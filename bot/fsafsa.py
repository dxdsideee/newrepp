import sqlite3
import random

conn = sqlite3.connect('base.db', check_same_thread=False)
cur = conn.cursor()
cur.execute('INSERT INTO ot VALUES (NULL, ?, ?, ?, ?)', (f'Бро, оба в касание! Благодарю', 'None', random.randint(4, 5), f'14.06.2022'))
conn.commit()