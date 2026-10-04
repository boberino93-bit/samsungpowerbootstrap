#!/usr/bin/env python3
import json
from pathlib import Path

EXPECTED_PROJECT = "fold7-power-lab"
EXPECTED_REPO = "boberino93-bit/samsungpowerbootstrap"
EXPECTED_ROOT = "/Fold7-PowerLab-AgentBus"

ALLOW = "ALLOW_PROJECT_LOCAL_WRITE"
DENY_AMBIGUOUS = "ASK_HUMAN_WRITE_NOWHERE"
DENY_MISMATCH = "DENY_PROJECT_SCOPE_MISMATCH"


def load_lock(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    required = {
        "mode": "FAIL_CLOSED",
        "project_id": EXPECTED_PROJECT,
        "canonical_writable_repository": EXPECTED_REPO,
        "coordination_root": EXPECTED_ROOT,
        "cross_project_write": "DENY",
    }
    for k, v in required.items():
        if data.get(k) != v:
            raise ValueError(f"identity lock mismatch: {k}")
    return data


def evaluate(intent_project_id, lock_path, proposed_repository=None, proposed_coordination_root=None):
    lock = load_lock(lock_path)
    if not intent_project_id:
        return {"allowed": False, "decision": DENY_AMBIGUOUS}
    if intent_project_id != lock["project_id"]:
        return {"allowed": False, "decision": DENY_MISMATCH}
    if proposed_repository and proposed_repository != lock["canonical_writable_repository"]:
        return {"allowed": False, "decision": DENY_MISMATCH}
    if proposed_coordination_root and proposed_coordination_root != lock["coordination_root"]:
        return {"allowed": False, "decision": DENY_MISMATCH}
    return {"allowed": True, "decision": ALLOW, "project_id": lock["project_id"], "repository": lock["canonical_writable_repository"], "coordination_root": lock["coordination_root"]}
