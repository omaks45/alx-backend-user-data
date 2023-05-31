#!/usr/bin/env python3
"""
an auth module
"""
from flask import request
from typing import List, TypeVar


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
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []
            return True
        if path is in excluded_paths:
            return False
        for exc_path in excluded_paths:
            if exc_path.startswith(path):
                return False
            elif path.startswith(exc_path):
                return False
            elif exc_path[-1] == "*":
                if path.startswith(exc_path[:-1]):
                    return False
            return True

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
