import sqlite3

con = sqlite3.connect("mydb.lite")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users (
name TEXT,
login TEXT,
pass TEXT
)""")

cur.execute("""
INSERT INTO users values("user3","user_3","1234")
""")

cur.execute("""INSERT INTO users values("user4","user_4","1234")""")
#
# cur.execute("""INSERT INTO users VALUES ('Miki', 'Miki67', '654')""")

con.commit()

data = cur.execute("SELECT * FROM users")
users = data.fetchone()
users2 = data.fetchone()

# users = data.fetchall()

# print(users, users2)

print("data obj", data)

for usr in data:
    print(usr)

con.close()