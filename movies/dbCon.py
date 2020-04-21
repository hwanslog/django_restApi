import sqlite3

try:
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    #cursor.execute("drop table test")
    # cursor.execute("create table test (name text,count integer)")
    # cursor.execute("insert into test(name,count) values('Terry',1)")
    # cursor.execute("insert into test(name,count) values('Cath',2)")
    # conn.commit()
    print("하이 ")
    result = cursor.execute("select * from HELLO")
    #rows = cursor.fetchall()
    while True:
        row = result.fetchone()
        if row == None:
            break
        print(row[0],row[1])
except sqlite3.Error:
    if conn:
        conn.rollback
finally:
    if conn:
        conn.close()