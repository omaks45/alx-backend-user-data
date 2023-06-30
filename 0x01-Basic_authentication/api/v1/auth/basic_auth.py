#!/usr/bin/env python3
"""
Basic Authentication Api module
"""

from typing import TypeVar
from api.v1.auth.auth import Auth
import base64

from models.user import User


class BasicAuth(Auth):
    """_summary_
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Args:
                 authorization_header (str): _description_
        Returns:
                 str: _description_
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic'):
            return None

        Heads = authorization_header.split(' ')[-1]
        return Heads
