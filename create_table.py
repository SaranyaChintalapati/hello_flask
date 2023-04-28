import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('DROP TABLE IF EXISTS register')
conn.commit()

conn.execute('DROP TABLE IF EXISTS address')
conn.commit()

conn.execute('DROP TABLE IF EXISTS payment')
conn.commit()

conn.execute('CREATE TABLE register(email TEXT, password TEXT, confirm_password TEXT)')
print("Created register table successfully!")

conn.execute('CREATE TABLE address(name TEXT, email TEXT, address TEXT, city TEXT, state TEXT, zip NUMBER)')
print("Created address table successfully!")

conn.execute('CREATE TABLE payment(card NUMBER, exp_month NUMBER, year TEXT, cvv NUMBER)')
print("Created payment table successfully!")

conn.close()