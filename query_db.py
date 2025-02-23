import sqlite3

DATABASE = 'applicants.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute("SELECT * FROM applicants")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()