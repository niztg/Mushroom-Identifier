""""
Test file
"""

import sqlite3
from datetime import datetime

from functions import AccountsDB
from classes import Account
import table

user1 = AccountsDB
account1 = user1.create_account(None, 'theCowardlyDog', 'luvMuriel123', 'courage@ramses.com', 11, 12, 1999, 1, 'courage')


#FIGURE OUT WHERE <account.db> IS WRITTEN INSTEAD OF <accounts.db> !!
