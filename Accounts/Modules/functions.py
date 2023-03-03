from datetime import datetime
from password import Password
from classes import Account
from exceptions import InvalidDateOfBirth
from exceptions import NotOldEnough
from exceptions import UsernameNotRightLength
from exceptions import EmailNotProper
from exceptions import UsernameTaken
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

# conn = sqlite3.connect('Databases/accounts.db')
# cursor = conn.cursor()

email_regex = re.compile(EMAIL_REGEX)

class AccountsDB:
    # def __init__(self):
    #     self.conn = sqlite3.connect('accounts.db')
    #     self.cursor= self.conn.cursor()

    #     self.cursor.execute('''CREATE TABLE IF NOT EXISTS account_info (
    #     account_name TEXT
    #     display_name TEXT
    #     password TEXT
    #     email TEXT
    #     dob integer
    #     id integer
    #     ) 
    #     ''')
    #     self.conn.commit()

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
        if len(str(mm))!=2 or len(str(dd))!=2 or len(str(yyyy))!=4:
            raise InvalidDateOfBirth()
        else:
            return datetime(*map(int, [yyyy, mm, dd]))
        
    def create_account(self, username: str, password: str, email: str, mm: int, dd: int, yyyy: int, id: int, display_name: str):
        """
        Creates an account.
        Args:
            username: str
            password: str
            email: str
            display_name: str
            id: int
        Returns:
            None
        """

        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()

        #hashing password
        hash = Password()
        password_hashed = hash.hashing(password)
        
        if not (6 <= len(username) <= 20) or not (1 <= len(display_name) <= 15 if display_name else True):
            raise UsernameNotRightLength()

        date = AccountsDB.dob_creator(int(mm), int(dd), int(yyyy))

        if not ((datetime.now() - date).days / 365) >= 13:
            raise NotOldEnough()

        if not (check := email_regex.search(email)) or not (check.end() - check.start() == len(email)):
            raise EmailNotProper()

        cursor.execute('INSERT INTO account_info (username, password, email, date_of_birth, display_name, id) VALUES (?, ?, ?, ?, ?, ?)',
                            (username, password_hashed, email, date, display_name, id))
        
        conn.commit()
        conn.close()
        user = Account()
        user_complete = user.retrieve_info(id)