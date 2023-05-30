#!/usr/bin/env python3
"""
Handling personal data
"""
import logging
from typing import List
import re

PIIS_FIELD = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Replaces vital information in a message  with a redacted
    value based on the list of field
    Args:
        fields: list of fields to redact
        redaction: the value to use for redaction
        message: the string message to filter
        separator: the separator to use between fields
    """
    for x in fields:
        message = re.sub(f'{x}=.*?{separator}',
                         f'{x}={redaction}{separator}', message)

    return message
