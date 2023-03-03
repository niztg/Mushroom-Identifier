"""
Note related functions
"""

from ...Accounts.Modules.classes import Account
from datetime import datetime

def create_note(author: Account, content: str):
    """
    Create a note
    """
    current_date = str(datetime.now())
