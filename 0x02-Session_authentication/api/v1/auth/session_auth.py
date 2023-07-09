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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """_user id for session id_
        Args:
            session_id(str, optional): _description_
        Returns:
            user id for sessional id
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        session id for user identification
        Args:
            request(_type_): _description_
        Returns:
            user instance based on user id
        """
        session_cookie = self.session(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user
