from datetime import datetime

def log_event(case, message):
    entry = {
        "time": datetime.utcnow().isoformat(),
        "event": message
    }
    case["timeline"].append(entry)
