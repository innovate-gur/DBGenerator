import sqlite3
import os


os.system("rm BDcode.db")
con = sqlite3.connect('BDcode.db')

curs = con.cursor()

curs.execute("create table BD( ID, Literal)")

curs.execute("insert into BD values( '001', 'youtube.com' )")

con.commit()

rows = curs.execute("select ID, Literal from BD")
for row in rows:
    print(row)