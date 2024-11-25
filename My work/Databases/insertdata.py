import sqlite3

con = sqlite3.connect("lecture.db")
cur = con.cursor()

#sql = "select * from student"
#result = cur.execute(sql)
#print(f" first row: {result.fetchone()}")

sgl = "insert into student values ('Mary', 'SD', 'Female')"
cur.execute(sgl)
con.commit()

#sql = "select * from student"
#result = cur.execute(sql)
#print(f" first row: {result.fetchone()}")

con.close()
