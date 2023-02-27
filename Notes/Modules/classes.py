"""
Where the note classes live.
"""

from Accounts.Modules.classes import Account
from datetime import datetime

class Note:
    """
    Defines the note class.
    Attributes:
        author: Account = The author of the note
        content: str = The content of the note
        date: datetime = Date the note was created
    """
    def __init__(self, author: Account, content: str, date: datetime):
        """
        Initializes the class
        """
        self._author = author
        self._content = content
        self._date = date

    # to do: everything
    