import sqlite3
con = sqlite3.connect("pfda.pd") # I will call this databbase pdfa.db
cur = con.cursor()

sql = "DROP TABLE IF EXISTS book"
cur.execute(sql)

cur.execute("CREATE TABLE book(title, author, ISBN)")
con.close()

result = cur.execute("SELECT * FROM books")
print("Books Table contents")
print(result.fetchone())
print("End of Books Table contents")