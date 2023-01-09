""""
Test file!
"""

import sqlite3

conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE account_info (
#     account_name text,
#     password text,
#     date_created text,
#     id text
# )""")

name = "Hello_worlder"
_dict = {
    "account_name": "recyclops",
    "password": "Hello",
    "date_created": "221229",
    "id": "32072"
}

# cursor.execute("INSERT INTO account_info VALUES (:account_name, :password, :date_created, :id)", _dict)

cursor.execute("SELECT * FROM account_info WHERE account_name='recyclops'")
information = cursor.fetchall()

print(cursor.execute("SELECT * FROM account_info").fetchall())

print(information)
conn.commit()
conn.close()