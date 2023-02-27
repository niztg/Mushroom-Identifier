"""
Classes
"""
from .exceptions import * 
from datetime import datetime

__all__ = (
    'Account'
)

class Account:
    """
    Defines an account   
    Attributes:
        name: str = The user's account name
        display_name[Optional]: str = the user's display name
        password: str = The user's password
        email: str = The user's email ID
        dob: str = The user's date of birth
    """
    def __init__(self, name: str, password: str, email: str, dob: datetime, display_name=None):
        """
        Initializes the class
        """
        self._name = name
        self._display_name = display_name
        self._password = password
        self._email = email
        self._dob = dob

    @classmethod
    def from_username_password(cls, username, password):
        """
        Initializes class from username and password
        Args:
            username: str
            password: str
        Returns:
            Account
        """
        ...
        # to add: finish this

    # to add: note functions (when the time comes)