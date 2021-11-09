# SQLite 嵌入式数据库，只有一个文件 如 data.db
# 经常用来集成到各种APP 中，甚至在操作系统中： Android、Linux、iOS、Mac OS等
# python 内置了 SQLite ，直接使用
# 数据库：多个二维表格，通过外键关联
# 第一步：connection
# 第二步：cursor.execute(SQL)
# 最后：关闭连接

import sqlite3
db_file = "scores.db"
conn = sqlite3.connect(db_file)

# 插入数据
def insert_score_data():
    cur = conn.cursor()
    sql = 'insert into score (stu_name, math_score, chinese_score) \
        values (?, ?, ?)'
    
    # 插入数据时，需要使用元组或者列表类型
    datas = [("关羽", 70, 65), ("子龙", 90, 90), ("张飞", 60, 60)]
    for data in datas:
        cur.execute(sql, data)
    
    # 提交数据
    conn.commit()
    cur.close()
    conn.close()

# 删除数据
def del_score_data():
    cur = conn.cursor()
    sql = 'delete from score where id=?'
    
    # 构建元组
    id = (4,)
    cur.execute(sql, id)
    conn.commit()  # 用连接提交，而不是游标
    cur.close()
    conn.close()

# 修改数据
def update_score_data():
    cur = conn.cursor()
    sql = 'update score set math_score = ?, chinese_score = ? where id = ?'

    # 构建元组数据
    data = (88, 88, 1)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()

# 查询数据
def select_score_data():
    cur = conn.cursor()
    sql = 'select * from score'
    cur.execute(sql)
    print(cur.fetchall())
    cur.close()
    conn.close()

# 批量插入多条数据
# 准备数据
score_list = [
    ('周瑜', 80, 70), 
    ('关胜', 68, 69),
    ('张苞', 50, 59),
    ('庞统', 100, 100),
    ('陆逊', 99, 99)
]

def insert_mul_data():
    cur = conn.cursor()
    sql = 'insert into score (stu_name, math_score, chinese_score) values (?, ?, ?)'
    # 插入多条记录要使用 executemany
    cur.executemany(sql, score_list)
    conn.commit()
    cur.close()
    conn.close()
    return cur.rowcount


# insert_score_data()
# del_score_data()
# update_score_data()
# select_score_data()
print(insert_mul_data())