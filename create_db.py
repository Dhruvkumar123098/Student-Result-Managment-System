import sqlite3
def create_db():
    con=sqlite3.connect(database='images.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,fee text,description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,Email text,Gender text,DOB text,Contact text,Admission text,Course text,City text,State text,Address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks_ob text,full_marks text,percentage text)")

    con.commit()

    con.close()
create_db()










