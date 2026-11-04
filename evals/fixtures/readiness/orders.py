import csv
import io


def matching_orders(rows, status):
    return [row for row in rows if status is None or row["status"] == status]


def visible_rows(rows, status=None, page=1, page_size=20):
    matches = matching_orders(rows, status)
    start = (page - 1) * page_size
    return matches[start:start + page_size]


def export_orders(rows, status=None, page=1, page_size=20):
    raise NotImplementedError
