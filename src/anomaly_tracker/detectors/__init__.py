"""Anomaly detectors.

Each detector takes a transactions DataFrame and returns a flags DataFrame
with columns: transaction_id, rule_id, severity, reason.
Active detectors are registered in DETECTORS.
"""

DETECTORS: list = []
