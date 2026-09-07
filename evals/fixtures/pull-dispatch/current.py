import random


def choose_worker(loads, candidate_count=8):
    """loads is a periodically refreshed snapshot of active work per instance."""
    candidates = sorted(loads, key=loads.get)[:candidate_count]
    if not candidates:
        raise RuntimeError("No available worker")
    return random.choice(candidates)


def submit_task(task, loads, gateway, counters, executor):
    worker = choose_worker(loads)
    receipt = gateway.start_task(worker, task)
    executor.submit(counters.record_active, task["id"])
    return {"accepted": True, "receipt": receipt}


def on_completed(task_id, counters):
    counters.record_finished(task_id)
