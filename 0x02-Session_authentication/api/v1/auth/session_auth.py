#!/usr/bin/env python3
"""
Module for sessional authentication
"""

from .auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """_empty session class_
    """
