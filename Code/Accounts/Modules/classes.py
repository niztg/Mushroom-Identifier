"""
Classes
"""

from datetime import datetime
import sqlite3

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
    def __init__(self, account_name: str, password: str, email: str, dob: datetime, id: int, display_name=None):
        """
        Initializes the class
        """
        # written by: niz
        self._name = account_name
        self._display_name = display_name
        self._password = password
        self._email = email
        self._dob = dob
        self._id = id

    @classmethod
    def retrieve_info(cls, id: int):
        # written by: khalid
        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()

        cursor.execute('SELECT account_name, password, email, dob, id, display_name FROM account_info WHERE id = ?', (id,))
       
        data = cursor.fetchone()
        
        conn.close()
        return cls(*data)

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
