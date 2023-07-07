#!/usr/bin/env python3
"""
Module for sessional authentication
"""

from .auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """_session class_
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """_creates session id for user_id
        Args:
            user_id(str, optional): _description_
        Returns:
            str(sessional_id)
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        Session_ID = str(uuid4())
        self.user_id_by_session_id[Session_ID] = user_id
        return Session_ID
