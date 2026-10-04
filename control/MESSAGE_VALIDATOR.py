#!/usr/bin/env python3
from datetime import datetime, timezone

PROJECT = "fold7-power-lab"
PROTOCOL = "1.0.0-alpha.1"

ACCEPTED = "ACCEPTED"
REJECTED = "REJECTED"
EXPIRED = "EXPIRED"
UNAUTHORIZED = "UNAUTHORIZED"
PROTOCOL_MISMATCH = "PROTOCOL_MISMATCH"
DUPLICATE = "DUPLICATE"

REQUIRED = {"protocol_version","message_id","sender","destination","message_type","created_at","payload"}


def _parse_time(value):
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    return datetime.fromisoformat(value)


def validate(message, bound_project_id=PROJECT, seen_ids=None, now=None):
    missing = sorted(REQUIRED - set(message))
    if missing:
        return {"result": REJECTED, "reason": f"missing:{','.join(missing)}"}
    if message.get("protocol_version") != PROTOCOL:
        return {"result": PROTOCOL_MISMATCH}
    sender = message.get("sender") or {}
    dest = message.get("destination") or {}
    if sender.get("project_id") != bound_project_id or dest.get("project_id") != bound_project_id:
        return {"result": UNAUTHORIZED, "reason": "project_identity_mismatch"}
    if message.get("task") and message["task"].get("project_id") not in (None, bound_project_id):
        return {"result": UNAUTHORIZED, "reason": "task_project_mismatch"}
    if seen_ids is not None and message["message_id"] in seen_ids:
        return {"result": DUPLICATE}
    exp = message.get("expires_at")
    if exp:
        now = now or datetime.now(timezone.utc)
        if _parse_time(exp) <= now:
            return {"result": EXPIRED}
    return {"result": ACCEPTED}
