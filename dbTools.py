import sqlite3
from sqlite3 import Error

# 连接数据库
def conn_db(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    if conn is not None:
        return conn

# 关闭连接
def close_db_conn(cur, conn):
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()