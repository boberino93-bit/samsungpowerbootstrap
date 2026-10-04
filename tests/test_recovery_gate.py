import json
from pathlib import Path

def test_risky_mutation_blocked_until_validated():
    d=json.loads(Path('.interagent/recovery/DEVICE_RECOVERY_CONTRACT.json').read_text())
    assert d['readiness']=='UNVALIDATED'
    assert d['blocks']['risky_persistent_device_mutation'] is True
    assert d['blocks']['boot_or_systemui_mutation'] is True
