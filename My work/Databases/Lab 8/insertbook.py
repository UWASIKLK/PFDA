import sqlite3
con = sqlite3.connect("pfda.db")
cur = con.cursor()

# checking if there is nothing in database
result = cur.execute("select * from book")
print(result.fetchone())

# insert a book
sql = """
    INSERT INTO book VALUES
        ('Harry Pothead', 'Just Kidding Really', "112344),
        ('Harry Potter does something profound', 'JK Rowling', "123444")
"""
# Danger!! this can lead to SQL injection
cur.execute(sql)
con.commit()
# something is missing here

result = cur.execute("select * from book")
print (result.fetchone())
con.close()
