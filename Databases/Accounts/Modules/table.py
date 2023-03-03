'''
Account info Table
NOT NEEDED ANYMORE
'''
# written by: khalid

import sqlite3

# # conn = sqlite3.connect('accounts.db')
# # cursor = conn.cursor()
# # if True:
# #     cursor.execute("""CREATE TABLE account_info (
# #         account_name text
# #         display text
# #         password text
# #         email text
# #         dobm text
# #         dobd text
# #         doby text
        
        
# #         )""")
    
# # False
# # conn.commit()
# # conn.close()


conn = sqlite3.connect('accounts.db')
cursor= conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS account_info (
account_name TEXT
display_name TEXT
password TEXT
email TEXT
dob integer
id integer
) 
''')
conn.commit()
