
import sqlite3
conn = sqlite3.connect('mydb.db') 
ins1 = '''
        insert into student(sname,sid,sclass,semail) values
        ('Mahendra','1201','12th','mr@gmail.com')
    '''
ins2 = '''
        insert into facult(fname,fid,fcourse,semail) values
        ('Sameer','3247','EM','sameer54@gmail.com')
    '''

conn.execute(ins1)
conn.execute(ins2)
conn.commit()
conn.close()