import sqlite3
from dbTools import conn_db, close_db_conn

db_file = "scores.db"

def select_score_data():
    conn = conn_db(db_file)
    cur = conn.cursor()
    sql = 'select * from score'
    cur.execute(sql)
    print(cur.fetchall())
    close_db_conn(cur, conn)

select_score_data()