#!/usr/bin/env python3
import argparse, hashlib, json, zipfile
from pathlib import Path

ROLES = {"PRIMARY":"PRIMARY.md","MANAGER":"MANAGER.md","RESEARCH":"RESEARCH.md"}
COMMON = [
    "PROJECT_IDENTITY_LOCK.json","AGENT_BOOTSTRAP.json","AGENT_BOOTSTRAP.md","BOOTSTRAP_ORDER.json","PROJECT_MANIFEST.json","VERSION.json",
    "control/PROJECT_SCOPE_GATE.py","control/MESSAGE_VALIDATOR.py","control/CAPABILITIES.json",
    "protocol/README.md","protocol/message-envelope.schema.json","protocol/task.schema.json","protocol/artifact.schema.json",
    ".interagent/recovery/DEVICE_RECOVERY_CONTRACT.json",".interagent/recovery/RECOVERY.md","docs/SAFETY_MODEL.md"
]

def sha(b): return hashlib.sha256(b).hexdigest()

def build(root, out, source_revision):
    version=json.loads((root/"VERSION.json").read_text())
    lock=json.loads((root/"PROJECT_IDENTITY_LOCK.json").read_text())
    bootstrap=json.loads((root/"AGENT_BOOTSTRAP.json").read_text())
    if bootstrap["project_id"] != lock["project_id"]:
        raise AssertionError("bootstrap/identity-lock project mismatch")
    if bootstrap["repository"]["full_name"] != lock["canonical_writable_repository"]:
        raise AssertionError("bootstrap/identity-lock repository mismatch")
    out.mkdir(parents=True, exist_ok=True)
    built=[]
    for role, role_file in ROLES.items():
        name=f"fold7-power-lab-{role.lower()}-agent-{version['package_version']}.zip"
        target=out/name
        hashes={}
        with zipfile.ZipFile(target,"w",compression=zipfile.ZIP_DEFLATED) as z:
            for rel in COMMON+[f".interagent/roles/{role_file}"]:
                b=(root/rel).read_bytes(); hashes[rel]=sha(b); z.writestr(rel,b)
            manifest={
                "schema":"fold7-power-lab/package-manifest/v1",
                "project_id":lock["project_id"],
                "canonical_repository":lock["canonical_writable_repository"],
                "role":role,
                "project_version":version["project_version"],
                "protocol_version":version["protocol_version"],
                "package_version":version["package_version"],
                "source_revision":source_revision,
                "capability_source":"control/CAPABILITIES.json",
                "bootstrap_first_steps":["project_scope_selection","identity_lock_validation","recovery_contract_load"],
                "integrity":{"files_sha256":hashes}
            }
            z.writestr("MANIFEST.json",json.dumps(manifest,indent=2,sort_keys=True)+"\n")
        built.append(target)
    return built

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--root",default="."); p.add_argument("--out",default="dist"); p.add_argument("--source-revision",required=True)
    a=p.parse_args();
    for x in build(Path(a.root),Path(a.out),a.source_revision): print(x)
