# app/auth.py

import os

VALID_KEYS = set([
    "demo-key-001",
    "demo-key-002",
    "test-api-key-123",
    "secure-access-key"
])

def verify_key(key: str) -> bool:
    """
    Check if the provided API key is valid.
    """
    return key in VALID_KEYS
