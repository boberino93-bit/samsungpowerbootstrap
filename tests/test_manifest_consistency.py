import json
from pathlib import Path

def test_identity_consistency():
    lock=json.loads(Path('PROJECT_IDENTITY_LOCK.json').read_text())
    manifest=json.loads(Path('PROJECT_MANIFEST.json').read_text())
    version=json.loads(Path('VERSION.json').read_text())
    assert lock['project_id']==manifest['project_id']==version['project_id']=='fold7-power-lab'
    assert lock['canonical_writable_repository']==manifest['repository_identity']=='boberino93-bit/samsungpowerbootstrap'
