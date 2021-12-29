import sqlite3 as sql

dbname = 'mydata.sqlite'

print("connecting to", dbname)
conn = sql.connect(dbname)

print("fetching data from customer table:")
cur = conn.execute('''
    select * 
    from customer''')

#for record in cur:
#    print(record)

