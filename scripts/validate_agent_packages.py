#!/usr/bin/env python3
import argparse, hashlib, json, zipfile
from pathlib import Path

PROJECT="fold7-power-lab"; REPO="boberino93-bit/samsungpowerbootstrap"; PROTOCOL="1.0.0-alpha.1"
ROLE_FILE={"PRIMARY":".interagent/roles/PRIMARY.md","MANAGER":".interagent/roles/MANAGER.md","RESEARCH":".interagent/roles/RESEARCH.md"}
BASE_REQUIRED={"PROJECT_IDENTITY_LOCK.json","AGENT_BOOTSTRAP.json","AGENT_BOOTSTRAP.md","BOOTSTRAP_ORDER.json","PROJECT_MANIFEST.json","VERSION.json","control/PROJECT_SCOPE_GATE.py","control/MESSAGE_VALIDATOR.py","control/CAPABILITIES.json","protocol/message-envelope.schema.json",".interagent/recovery/DEVICE_RECOVERY_CONTRACT.json","MANIFEST.json"}

def sha(b): return hashlib.sha256(b).hexdigest()

def validate(path):
    with zipfile.ZipFile(path) as z:
        names=set(z.namelist()); m=json.loads(z.read("MANIFEST.json")); role=m.get("role")
        missing=(BASE_REQUIRED|{ROLE_FILE.get(role,"__invalid__")})-names
        assert not missing, f"missing {sorted(missing)}"
        assert m["project_id"]==PROJECT
        assert m["canonical_repository"]==REPO
        assert m["protocol_version"]==PROTOCOL
        assert m["bootstrap_first_steps"]==["project_scope_selection","identity_lock_validation","recovery_contract_load"]
        lock=json.loads(z.read("PROJECT_IDENTITY_LOCK.json")); bootstrap=json.loads(z.read("AGENT_BOOTSTRAP.json")); manifest=json.loads(z.read("PROJECT_MANIFEST.json"))
        assert lock["project_id"]==bootstrap["project_id"]==manifest["project_id"]==PROJECT
        assert lock["canonical_writable_repository"]==bootstrap["repository"]["full_name"]==manifest["repository_identity"]==REPO
        assert lock["cross_project_write"]=="DENY"
        for rel,expected in m["integrity"]["files_sha256"].items(): assert sha(z.read(rel))==expected, rel
        foreign=("project_id\": \"duo-open","project_id\": \"benefitflow","project_id\": \"warp-propulsion-lab")
        combined="\n".join(z.read(x).decode("utf-8","ignore").lower() for x in ["PROJECT_IDENTITY_LOCK.json","AGENT_BOOTSTRAP.json","PROJECT_MANIFEST.json",ROLE_FILE[role]])
        for token in foreign: assert token not in combined, f"foreign project authority token {token}"
    return True

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("archives",nargs="+"); a=p.parse_args()
    for f in a.archives: validate(Path(f)); print(f"PASS {f}")
