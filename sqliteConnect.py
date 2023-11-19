import sqlite3
conn = sqlite3.connect('mydb.db')  #database name = mydeb.db
#creating table
conn.execute('''
    create table student(
        sid int auto_increment primary key,
        sname varchar(30),
        semail varchar(30),
        sclass varchar(10)
    )
    ''')
#inserting values
