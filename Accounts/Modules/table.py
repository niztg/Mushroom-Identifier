'''
Account info Table
'''

import sqlite3

conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()
if True:
    cursor.execute("""CREATE TABLE account_info (
        account_name text
        display text
        password text
        email text
        dobm text
        dobd text
        doby text
        
        
        )""")
    
False
conn.commit()
conn.close()