""""
Test file
"""

import sqlite3
from datetime import datetime

from Modules.functions import AccountsDB
from Modules.classes import Account

user1 = AccountsDB
account1 = user1.create_account("theCowardlyDog", "luvMuriel123", "courage@ramses.com", "11", "12", "1999", "courage", 1)