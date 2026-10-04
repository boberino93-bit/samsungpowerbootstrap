from datetime import datetime, timezone, timedelta
from control.MESSAGE_VALIDATOR import validate, ACCEPTED, UNAUTHORIZED, EXPIRED, DUPLICATE

def msg():
    return {"protocol_version":"1.0.0-alpha.1","message_id":"fold7-msg-00000001","sender":{"project_id":"fold7-power-lab","agent_id":"a","agent_instance_id":"i","role":"RESEARCH"},"destination":{"project_id":"fold7-power-lab","channel":"research"},"message_type":"CHECKPOINT","created_at":"2026-10-04T00:00:00Z","payload":{}}

def test_accept(): assert validate(msg())["result"]==ACCEPTED

def test_cross_project_reject():
    x=msg(); x["destination"]["project_id"]="benefitflow"; assert validate(x)["result"]==UNAUTHORIZED

def test_duplicate(): assert validate(msg(),seen_ids={"fold7-msg-00000001"})["result"]==DUPLICATE

def test_expired():
    x=msg(); x["expires_at"]="2026-10-03T00:00:00Z"; assert validate(x,now=datetime(2026,10,4,tzinfo=timezone.utc))["result"]==EXPIRED
