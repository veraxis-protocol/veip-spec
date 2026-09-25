#!/usr/bin/env python3
"""
Independent adjudication analysis for DICE_1000_AGENT_EQUIVALENT_DEMO_001 (v3).

Does NOT modify the audited source. Imports dice_1000_demo_v3_strict_locality as a
module and observes it through wrappers only. Every instrumented run is checked to
return exactly the same per-run result dict as an uninstrumented run.
"""
import ast, importlib.util, json, math, statistics, sys
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("v3", root / "dice_1000_demo_v3_strict_locality.py")
v3 = importlib.util.module_from_spec(spec); sys.modules["v3"] = v3; spec.loader.exec_module(v3)
MODES = ("random", "targeted_high_degree", "targeted_local_cut")
SEEDS = range(1000, 1010)
out = {}

# ---------------------------------------------------------------- 1. static audit
src = (root / "dice_1000_demo_v3_strict_locality.py").read_text()
tree = ast.parse(src)
fn = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
names_in_recover = sorted({n.id for n in ast.walk(fn["recover_one"]) if isinstance(n, ast.Name)})
attrs_in_recover = sorted({f"{n.value.id}.{n.attr}" for n in ast.walk(fn["recover_one"])
                           if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name)})
out["static_audit"] = {
    "recover_one_names": names_in_recover,
    "recover_one_attribute_access": attrs_in_recover,
    "recover_one_references_failed_adj_states": sorted(set(names_in_recover) & {"failed", "adj", "states"}),
    "recover_one_touches_private_net_fields": [a for a in attrs_in_recover if "._" in a],
}

# ---------------------------------------------------------------- 2. instrumented runs
orig_recover = v3.recover_one
orig_detect = v3.local_detection_events
orig_probe = v3.LocalNetwork.probe
orig_send = v3.LocalNetwork.send
orig_state = v3.LocalNetwork.local_state
orig_claim = v3.LocalNetwork.try_claim

class Rec:
    def reset(self):
        self.per_task = []          # per recovery: dict
        self.cur = None
        self.oracle_reads_during_recovery = 0
R = Rec()

def w_recover(net, detector, task, radius, max_visits):
    before_msgs = net.messages
    R.cur = {"touched": set(), "checks": 0, "probes": 0, "probes_dead": 0, "forwards": 0,
             "forward_recipients": set(), "claimed": None}
    res = orig_recover(net, detector, task, radius, max_visits)
    R.cur["messages"] = net.messages - before_msgs
    R.cur["recovered"] = res[0] is not None
    R.cur["hop"] = res[1]
    R.per_task.append(R.cur); R.cur = None
    return res

def w_probe(self, src, dst):
    a = orig_probe(self, src, dst)
    if R.cur is not None:
        R.cur["probes"] += 1; R.cur["probes_dead"] += (not a); R.cur["touched"] |= {src, dst}
    return a

def w_send(self, src, dst, et, tid, hop):
    ok = orig_send(self, src, dst, et, tid, hop)
    if R.cur is not None:
        R.cur["forwards"] += 1; R.cur["forward_recipients"].add(dst); R.cur["touched"] |= {src, dst}
    return ok

def w_state(self, requester):
    if R.cur is not None:
        R.cur["checks"] += 1; R.cur["touched"].add(requester)
    return orig_state(self, requester)

def w_claim(self, node, task):
    ok = orig_claim(self, node, task)
    if R.cur is not None and ok:
        R.cur["claimed"] = node
    return ok

def instrumented(n, seed, mode, **kw):
    R.reset()
    v3.recover_one = w_recover
    v3.LocalNetwork.probe, v3.LocalNetwork.send = w_probe, w_send
    v3.LocalNetwork.local_state, v3.LocalNetwork.try_claim = w_state, w_claim
    try:
        r = v3.run_one(n, seed, mode, **kw)
    finally:
        v3.recover_one = orig_recover
        v3.LocalNetwork.probe, v3.LocalNetwork.send = orig_probe, orig_send
        v3.LocalNetwork.local_state, v3.LocalNetwork.try_claim = orig_state, orig_claim
    return r, list(R.per_task)

# fidelity check: instrumentation must not change results
for mode in MODES:
    a = v3.run_one(1000, 1000, mode); b, _ = instrumented(1000, 1000, mode)
    assert a == b, f"instrumentation changed result for {mode}"
out["instrumentation_fidelity"] = "PASS (instrumented run_one == uninstrumented run_one, n=1000 seed=1000, all modes)"

# ---------------------------------------------------------------- 3. headline + decomposition at n=1000
def ci95(xs):
    m = statistics.mean(xs); s = statistics.stdev(xs); h = 2.262 * s / math.sqrt(len(xs))  # t(0.975, 9)
    return {"mean": m, "sd": s, "ci95": [m - h, m + h], "min": min(xs), "max": max(xs)}

head = {}
for mode in MODES:
    runs = []; tasks = []
    for s in SEEDS:
        r, pt = instrumented(1000, s, mode)
        runs.append(r); tasks.append(pt)
    flat = [t for pt in tasks for t in pt]
    n = 1000
    msg_checks = sum(t["checks"] for t in flat); msg_probes = sum(t["probes"] for t in flat)
    msg_fwd = sum(t["forwards"] for t in flat); msg_claim = sum(1 for t in flat if t["recovered"])
    total = sum(r["recovery_messages"] for r in runs)
    assert msg_checks + msg_probes + msg_fwd + msg_claim == total, "message decomposition mismatch"
    per_task_fp = [len(t["touched"]) for t in flat]
    # TDD MET-011 reading: agents whose coordination/control state CHANGES
    state_change_claims = [sum(1 for t in pt if t["recovered"]) / n for pt in tasks]
    state_change_incl_fwd = []
    for pt in tasks:
        s_ = set()
        for t in pt:
            s_ |= t["forward_recipients"]
            if t["claimed"] is not None: s_.add(t["claimed"])
        state_change_incl_fwd.append(len(s_) / n)
    unrec = [t for t in flat if not t["recovered"]]
    head[mode] = {
        "local_msr": ci95([r["local_msr"] for r in runs]),
        "central_msr_mean": statistics.mean(r["central_msr"] for r in runs),
        "reassignment_completion": ci95([r["reassignment_completion_rate"] for r in runs]),
        "detection_events_mean": statistics.mean(r["local_detection_events"] for r in runs),
        "failed_agents": runs[0]["failed_agents"],
        "recovery_messages_mean": statistics.mean(r["recovery_messages"] for r in runs),
        "messages_per_failed_task_mean": statistics.mean(r["messages_per_failed_task"] for r in runs),
        "neighbor_probes_mean": statistics.mean(r["neighbor_probes"] for r in runs),
        "role_binding_violations_total": sum(r["role_binding_violations"] for r in runs),
        "message_mix_fraction": {"local_candidate_check": msg_checks / total, "neighbor_probe": msg_probes / total,
                                 "search_forward": msg_fwd / total, "claim": msg_claim / total},
        "probes_to_dead_nodes_fraction": sum(t["probes_dead"] for t in flat) / msg_probes,
        "perturbation_locality_as_coded_mean": statistics.mean(r["perturbation_locality"] for r in runs),
        "per_recovery_footprint_nodes": {"mean": statistics.mean(per_task_fp), "median": statistics.median(per_task_fp),
                                         "max": max(per_task_fp), "fraction_of_n_mean": statistics.mean(per_task_fp) / n},
        "state_change_fraction_claims_only_mean": statistics.mean(state_change_claims),
        "state_change_fraction_claims_plus_forward_recipients_mean": statistics.mean(state_change_incl_fwd),
        "candidate_checks_per_recovery_mean": statistics.mean(t["checks"] for t in flat),
        "candidate_checks_per_UNRECOVERED_task_mean": statistics.mean(t["checks"] for t in unrec) if unrec else None,
        "unrecovered_tasks_total": len(unrec),
        "recovery_hops_distribution": dict(sorted(Counter(t["hop"] for t in flat if t["recovered"]).items())),
    }
out["n1000"] = head

# ---------------------------------------------------------------- 4. independent recomputation from raw file
raw = [json.loads(l) for l in (root / "fresh/v3/raw_runs.jsonl").read_text().splitlines() if l.strip()]
recomp = {}
for mode in MODES:
    xs = [r for r in raw if r["n"] == 1000 and r["failure_mode"] == mode]
    recomp[mode] = {k: statistics.mean(r[k] for r in xs) for k in
                    ("local_msr", "reassignment_completion_rate", "recovery_messages", "messages_per_failed_task",
                     "perturbation_locality", "neighbor_probes")}
slopes = {}
for mode in MODES:
    pts = []
    for n in (250, 500, 1000, 2000):
        xs = [r for r in raw if r["n"] == n and r["failure_mode"] == mode]
        pts.append((math.log(n), math.log(statistics.mean(r["recovery_messages"] for r in xs))))
    xm = sum(p[0] for p in pts) / 4; ym = sum(p[1] for p in pts) / 4
    slopes[mode] = sum((x - xm) * (y - ym) for x, y in pts) / sum((x - xm) ** 2 for x, _ in pts)
per_task_by_n = {mode: {n: statistics.mean(r["messages_per_failed_task"] for r in raw if r["n"] == n and r["failure_mode"] == mode)
                        for n in (250, 500, 1000, 2000)} for mode in MODES}
reassign_by_n = {mode: {n: statistics.mean(r["reassignment_completion_rate"] for r in raw if r["n"] == n and r["failure_mode"] == mode)
                        for n in (250, 500, 1000, 2000)} for mode in MODES}
out["recomputed_from_raw_n1000"] = recomp
out["recomputed_loglog_slopes"] = slopes
out["messages_per_failed_task_by_n"] = per_task_by_n
out["reassignment_completion_by_n"] = reassign_by_n

# ---------------------------------------------------------------- 5. sensitivity (parameters only; source untouched)
sens = {}
for mv in (40, 80, 160, 320):
    row = {}
    for mode in MODES:
        rs = [v3.run_one(1000, s, mode, max_visits=mv) for s in SEEDS]
        row[mode] = {"reassign": statistics.mean(r["reassignment_completion_rate"] for r in rs),
                     "msgs_per_task": statistics.mean(r["messages_per_failed_task"] for r in rs),
                     "locality_as_coded": statistics.mean(r["perturbation_locality"] for r in rs)}
    sens[f"max_visits={mv}"] = row
out["sensitivity_max_visits_n1000"] = sens

# a genuinely localized, small perturbation: 1% local cut instead of 20%
small = {}
for frac in (0.01, 0.05):
    rs = [v3.run_one(1000, s, "targeted_local_cut", fraction=frac) for s in SEEDS]
    small[f"local_cut_fraction={frac}"] = {
        "failed": rs[0]["failed_agents"],
        "reassign": statistics.mean(r["reassignment_completion_rate"] for r in rs),
        "locality_as_coded": statistics.mean(r["perturbation_locality"] for r in rs)}
out["small_localized_perturbation_n1000"] = small

(root / "claude_independent_analysis.json").write_text(json.dumps(out, indent=2, default=list) + "\n")
print(json.dumps(out, indent=2, default=list))
