#!/usr/local/bin/python3
import MySQLdb


db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="Root@890", db="db_test", charset="utf8")
cur = db.cursor()
#cur.execute("INSERT INTO students VALUES (15, 'ziza', 17, 12)")
cur.execute("update students SET name='aziza' where name='ziza'")
db.commit()
cur.execute("SELECT students.student_id , students.age, students.name, teachers.name from students join teachers on students.teacher_id = teachers.teacher_id")
query_rows = cur.fetchall()

for row in query_rows:
    print(row)










#from sqlalchemy import create_engine, Column, String, Integer
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker

#Base = declarative_base()

#class Students(Base):
    #__tablename__ = 'students'
    #id = Column(Integer, primary_key=True)
    #name = Column(String)
    #age = Column(Integer)


#engine = create_engine('sqlite:///students.db');

#session = sessionmaker(bind=engine)()

#update_student = session.query(Students).filter_by(id=4).first()

#if update_student:
    #update_student.name = 'ahmed'
    #session.commit()

#for user in session.query(Students).filter(Students.age >= 18, Students.age <= 27, Students.name == 'ahmed').all():
    #print(user.name, user.age)




#session.add(Students(name='aicha', age=12))
#session.add(Students(name='zahra', age=14))
#session.add(Students(name='noufal', age=20))
#session.commit()





#from sqlalchemy import create_engine, Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker

#Base = declarative_base()

#class User(Base):
    #__tablename__ = 'users'
    #id = Column(Integer, primary_key=True)
    #name = Column(String)
    #age = Column(Integer)

#user = User(name='khalid', age=28)

#engine = create_engine('sqlite:///example.db')
#Base.metadata.create_all(engine)

#Session = sessionmaker(bind=engine)()
#Session.add(user)
#Session.commit()
