import sqlite3

con = sqlite3.connect("lecture.db")
cur = con.cursor()

sgl = "CREATE TABLE student (name, course, gender)"
cur.execute(sgl)
con.close()