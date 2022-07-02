import sqlite3


conn = sqlite3.connect('base.db', check_same_thread=False)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   user_id INT PRIMARY KEY,
   balance INT,
   bills TEXT,
   amount INT,
   id INT,
   bill_id TEXT,
   text TEXT);
""")
conn.commit()

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS bills(
   user_id INT,
   bills TEXT,
   amount INT,
   bill_id TEXT PRIMARY KEY,
   text TEXT);
""")
conn.commit()

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS ot(
    otziv1 TEXT PRIMARY KEY,
    otziv2 TEXT,
    otziv3 TEXT,
    otziv4 TEXT,
    otziv5 TEXT,
    otziv6 TEXT,
    otziv7 TEXT)
""")
conn.commit()