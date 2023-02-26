from datetime import datetime
from .exceptions import *

import re
import sqlite3

all = (
    'dob_creator',
    'create_account'
)

EMAIL_REGEX = r"[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}"

# Sources for regex help:
# https://stackoverflow.com/questions/58560831/email-regex-within-python
# https://docs.python.org/3/library/re.html

conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()

email_regex = re.compile(EMAIL_REGEX)

def dob_creator(mm, dd, yyyy):
    """
    Checks if a valid date of birth has been entered
    Args:
        mm: month
        dd: day
        yyyy: year
    Returns:
        None if valid
        Error if invalid
    """
    try:
        return datetime(*map(int, [yyyy, mm, dd]))
    except:
        raise AttributeError()

def create_account(username: str, password: str, email: str, mm, dd, yyyy, display_name: str = None):
    """
    Creates an account.
    Args:
        username: str
        password: str
        email: str
        display_name: str
    Returns:
        None
    """
    if not (6 <= len(username) <= 20) or not (1 <= len(display_name) <= 15 if display_name else True):
        raise UsernameNotRightLength()

    date = dob_creator(mm, dd, yyyy)

    if not ((datetime.now() - date).days / 365) >= 13:
        raise NotOldEnough()

    if not (check := email_regex.search(email)) or not (check.end() - check.start() == len(email)):
        raise EmailNotProper()

    print("promt")
    
conn.commit()
conn.close()