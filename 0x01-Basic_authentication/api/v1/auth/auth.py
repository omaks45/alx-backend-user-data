#!/usr/bin/env python3
"""
an auth module
"""
from flask import request
from typing import List, Typevar


class Auth:
    """_summary_
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Args:
            path (str): _description_
            excluded_paths (List[str]): _description
        Returns:
            bool: _description_
        """

    def authorization_header(self, request=None) -> str:
        """_summary_
        Args:
            request (_tpye_, optional): _description_.Default to None
        """
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_
        """

        return None
