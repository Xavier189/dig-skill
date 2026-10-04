def dispatch(task, settings, counters, gateway):
    counters.record_attempt(task["id"])
    over_limit = counters.active() >= settings.limit
    if settings.enforce and over_limit:
        return {"accepted": False, "reason": "RATE_LIMITED"}
    receipt = gateway.send(task)
    counters.record_accepted(task["id"])
    return {"accepted": True, "receipt": receipt}


class Settings:
    enforce = True
    limit = 10
