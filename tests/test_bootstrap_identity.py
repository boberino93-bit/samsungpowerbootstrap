import json
from pathlib import Path

def test_bootstrap_matches_identity_lock():
    lock=json.loads(Path('PROJECT_IDENTITY_LOCK.json').read_text())
    boot=json.loads(Path('AGENT_BOOTSTRAP.json').read_text())
    manifest=json.loads(Path('PROJECT_MANIFEST.json').read_text())
    assert lock['project_id']==boot['project_id']==manifest['project_id']=='fold7-power-lab'
    assert lock['canonical_writable_repository']==boot['repository']['full_name']==manifest['repository_identity']=='boberino93-bit/samsungpowerbootstrap'
    assert boot['rules']['identity_lock_first'] is True
    assert boot['rules']['identity_conflict']=='STOP_BEFORE_MUTATION'
