import json, tempfile
from control.PROJECT_SCOPE_GATE import evaluate

LOCK={"mode":"FAIL_CLOSED","project_id":"fold7-power-lab","canonical_writable_repository":"boberino93-bit/samsungpowerbootstrap","coordination_root":"/Fold7-PowerLab-AgentBus","cross_project_write":"DENY"}

def path():
    f=tempfile.NamedTemporaryFile("w",delete=False); json.dump(LOCK,f); f.close(); return f.name

def test_local_allowed():
    assert evaluate("fold7-power-lab",path(),proposed_repository="boberino93-bit/samsungpowerbootstrap")["allowed"]

def test_ambiguous_denied():
    assert not evaluate(None,path())["allowed"]

def test_foreign_denied():
    assert not evaluate("duo-open",path(),proposed_repository="boberino93-bit/duo-open")["allowed"]
