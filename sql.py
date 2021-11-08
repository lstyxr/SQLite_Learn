# 1. 导入模块
import sqlite3

# 2. 数据库文件导入
db_file = "scores.db"

# 3. 连接数据库
conn = sqlite3.connect(db_file)

# 4. 编写 SQL 语句
sql = 'select * from score'

# 5. 执行 SQL
cur = conn.cursor()
cur.execute(sql)

# 6. 取得结果
print(cur.fetchall())

# 7. 关闭连接
conn.close()