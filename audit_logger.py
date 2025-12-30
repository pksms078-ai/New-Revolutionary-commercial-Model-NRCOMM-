import json
from datetime import datetime

def log_action(user, action, law, ai_output, decision):
    log = {
        "user": user,
        "action": action,
        "law_reference": law,
        "ai_output": ai_output,
        "human_decision": decision,
        "timestamp": datetime.now().isoformat()
    }
    with open("audit_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")
Add audit logging module

