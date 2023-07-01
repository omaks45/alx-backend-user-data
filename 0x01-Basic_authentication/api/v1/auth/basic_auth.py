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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """_summary_
        Args:
            authorization_header (str): _description_
        Returns:
                str: _description_
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            value_to_decode = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(value_to_decode)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Args:
                            self(_type_): _description_
                            str(_type_): _description_
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        email, password = decoded_base64_authorized_header.split(':')
        return (email, password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """_summary_
        Args:
                self(_type_): _description_
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
                return None
        except Exception:
            return None

     def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        Heads = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(Heads)
        email, password = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(email, password)
