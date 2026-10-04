def on_summary(summary, cache, output):
    detail = cache.get(summary["call_id"])
    output.send({
        "call_id": summary["call_id"],
        "wait_seconds": detail["queue_seconds"] if detail else 0,
    })


def on_detail(detail, cache):
    cache.put(detail["call_id"], detail)
