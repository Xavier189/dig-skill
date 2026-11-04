"""Fictional intake and resolution records for an evaluation fixture."""


def intake_status(accepted):
    """HTTP 200 means the intake request was accepted, before any agent handles it."""
    return 200 if accepted else 503


def resolution_state(customer_confirmed):
    """A later callback records whether the customer confirmed resolution."""
    return "resolved" if customer_confirmed else "pending"


SAMPLE = [
    {"http_status": 200, "resolution_state": "resolved"},
    {"http_status": 200, "resolution_state": "pending"},
    {"http_status": 200, "resolution_state": "pending"},
    {"http_status": 503, "resolution_state": "pending"},
]
