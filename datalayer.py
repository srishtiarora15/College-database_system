import pyodbc
from abc import ABC
from components import Course
from components import Session
from components import Subject
from components import Student
from components import SemesterSubject
from components import Enrollment


class DBOperations(ABC):
    def __init__(self):
        self.con=pyodbc.connect("Driver={SQL SERVER};Server=LAPTOP-77MU19DM\SRISHTI;database=ProjectDB;uid=sa;pwd=srishti")
        
class DALCourses(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
    def AddCourses(self, pro):
        cur=self.con.cursor()
        cur.execute("select * from course")
        query="insert into Course values(?,?)"
        print(pro.CourseName, pro.Description)
        row=(pro.CourseName, pro.Description)
        cur.execute(query, row)
        
        self.con.commit()
        
        
    def GetCourses(self):
        cur=self.con.cursor()
        cur.execute("select * from Course")
        records=cur.fetchall()
        
        AllCourses = []
        
        for record in records:
            pro=Course()
            pro.CourseID=record[0]
            pro.CourseName=record[1]
            pro.Description=record[2]
           
            
            AllCourses.append(pro)
            
        return AllCourses
        
    def DeleteCourse(self, CourseID):
        cur=self.con.cursor()
        
        query="delete from Course where CourseID=?"
        row=(CourseID)
        
        cur.execute(query, row)
        self.con.commit()
        
        
        
class DBSession(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
        
    def AddSession(self, ses):
        cur=self.con.cursor()
        
        query="insert into Session values(?)"
        row=(ses.Session)
        
        cur.execute(query, row)
        self.con.commit()
        
    def GetSession(self):
        cur=self.con.cursor()
        cur.execute("Select * from Session")
        
        records=cur.fetchall()
        AllSessions=[]
        
        
        for record in records:
            pro=Session()
            pro.SessionID=record[0]
            pro.Session=record[1]
            
            
            AllSessions.append(pro)
            
        return AllSessions
    
    def DeleteSession(self, c):
        cur=self.con.cursor()
        
        query="Delete from Session where SessionID=?"
        row=(c.SessionID)
        
        cur.execute(query, row )
        self.con.commit()
        
class DBSubject(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
        
    def AddSubject(self, sub):
        cur=self.con.cursor()
        
        query="Insert into Subject values(?, ?)"
        row = (sub.SubjectName, sub.Description)
        
        cur.execute(query, row)
        self.con.commit()
        
    def GetSubject(self):
        cur=self.con.cursor()
        cur.execute("select * from Subject")
        
        records =cur.fetchall()
        AllSubjects=[]
        
        for record in records:
            pro=Subject()
            pro.SubjectID=record[0]
            pro.SubjectName=record[1]
            pro.Description=record[2]
            
            AllSubjects.append(pro)
            
        return AllSubjects 
    
    def DeleteSubject(self, c):
        cur=self.con.cursor()
        
        query="delete from Subject where SubjectID=?"
        row=(c.SubjectID)

        cur.execute(query, row)
        self.con.commit() 

    def AddSemesterSubject(self, sem):
        cur=self.con.cursor()
        query="Insert into SemesterSubject values(?, ?, ?, ?)"
        row=(sem.SessionID, sem.CourseID, sem.Semester, sem.SubjectID)
        
        cur.execute(query, row)
        self.con.commit()
        
    def GetSemesterSubject(self):
        cur=self.con.cursor()
        cur.execute("select s.SemesterSubjectID, ss.Session, C.CourseName, s.Semester, n.SubjectName from SemesterSubject as [s], Session as [ss], Course as [c], Subject as [n] where s.SessionID=ss.SessionID and s.CourseID=c.CourseID and s.SubjectID=n.SubjectID")
        records =cur.fetchall()
        AllSemesterSubjects=[]
        
        for record in records:
            sem=SemesterSubject()
            sem.SemesterSubjectID=record[0]
            sem.SessionID=record[1]
            sem.CourseID=record[2]
            sem.Semester=record[3]
            sem.SubjectID=record[4]
            
            AllSemesterSubjects.append(sem)
            
        return AllSemesterSubjects 
    
    
    def DeleteSemesterSubject(self, SemesterSubjectID):
        cur=self.con.cursor()
        
        query="delete from SemesterSubject where SemesterSubjectID=?"
        row=(SemesterSubjectID)

        cur.execute(query, row)
        self.con.commit() 
        
            
            
        
        
class DBStudent(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
        
    def AddStudent(self, stu):
        cur=self.con.cursor()
        query = "Insert into Student values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        row=(stu.RollNo, stu.Date, stu.Name, stu.DOB, stu.Gender, stu.FatherName, stu.MotherName, stu.Address, stu.City, stu.ContactNo, stu.EmailID, stu.Nationality, stu.CourseID, stu.SessionID)
        cur.execute(query, row)
        self.con.commit()
   
    
    def GetStudent(self):
        cur=self.con.cursor()
        cur.execute("select s.RegistrationID,s.RollNo, s.Name, c.CourseName, ss.Session from Student as [s], Course as [c], Session as [ss] where s.CourseID=c.CourseID and s.SessionID=ss.SessionID")
        
        records =cur.fetchall()
        AllStudents=[]
        
        for record in records:
            stu=Student()
            stu.RegistrationID=record[0]
            stu.RollNo=record[1]
            stu.Name=record[2]
            stu.CourseID=record[3]
            stu.SessionID=record[4]
            
            AllStudents.append(stu)
            
        return AllStudents 
    
    def DeleteStudent(self, RegistrationID):
        cur=self.con.cursor()
        
        query="delete from Student where RegistrationID=?"
        row=(RegistrationID)

        cur.execute(query, row)
        self.con.commit() 
        
    def FindStudent(self, RollNo):
        cur = self.con.cursor()
        query="Select s.RegistrationID, s.RollNo, s.Name, s.FatherName, s.MotherName from Student as [s] where RollNo=?"
        row=(RollNo)
        cur.execute(query, row)
        records=cur.fetchall()
        
        AllStudents=[]
        
        for record in records :
            stu=Student()
            stu.RegistrationID=record[0]
            stu.RollNo=record[1]
            stu.Name=record[2]
            stu.FatherName=record[3]
            stu.MotherName=record[4]
            
            AllStudents.append(stu)
            
        return AllStudents
    
    def ViewStudent(self, sessid, cid, sem):
        cur=self.con.cursor()
        
        query="select * from Student where CourseID=? and SessionID=? and RegistrationID IN (Select RegistrationID from Enrollment where Semester=? and IsCurrent=1)"
        row=(cid, sessid, sem)
        
        cur.execute(query, row)
        records=cur.fetchall()
        
        AllDetails=[]
        
        for record in records:
            st=Student()
            st.RegistrationID=record[0]
            st.RollNo=record[1]
            st.Name=record[3]
            st.CourseID=record[4]
            st.SessionID=record[5]
            
            
            AllDetails.append(st)
            
            
        return AllDetails
            
            
class DALEnrollment(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
        
    def AddEnrollment(self, en):
        cur=self.con.cursor()
        
        query="Insert into Enrollment values(?, ?, ?, ?)"
        row = (en.Date, en.Semester, en.RegistrationID, 1)
        
        cur.execute(query, row)
        self.con.commit()
        
        
        
class DBMarks(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
        
    def AddMarks(self, marks,SemesterSubjectID, rid):
        cur=self.con.cursor()
        query="Insert into Marks values (?,?, ?, ?)"
        name = "s"
        row=(rid,name,SemesterSubjectID, marks)
        cur.execute(query, row)
        
        self.con.commit()
        
        
        
    def CheckMarks(self, rid, sem):
        cur=self.con.cursor()
        #cur.execute("select Marks from Marks where RegistrationID=?, RegistrationID")
        #cur.execute("select e.RegistrationID, e.Semester, ssub.SubjectID, m.Marks from Enrollment as [e], SemesterSubject as [ssub], Marks as m where e.Semester=ssub.Semester and ssub.SubjectID=m.SubjectID")
        cur.execute("select Marks from Marks as [m], SemesterSubject as [ss] where m.SemesterSubjectID=ss.SemesterSubjectID and  RegistrationID=? and ss.Semester=?", (rid, sem))
        records=cur.fetchall()
        AllMarks=[]
        
        for marks in records:
            AllMarks.append(marks[0])
            
        return AllMarks
        
    def GetSubjects(self, SessionID, CourseID, Semester):
        cur=self.con.cursor()
        #query="select ss.SessionID, c.CourseID, ssem.Semester, s.RegistrationID, ssub.SubjectID from Session as [ss], Course as [c], SemesterSubject as [ssem], Student as [s], Subject as [ssub] where s.SessionID=ss.SessionID and  s.CourseID=c.CourseID and ssub.SubjectID=ssem.SubjectID"
        query="select ss.SemesterSubjectID, s.SubjectName from SemesterSubject as [ss], Subject as [s]  where ss.SubjectID=s.SubjectID and  ss.SessionID=? and ss.CourseID=? and ss.Semester=?"
        row=(CourseID,SessionID, Semester)
        
        cur.execute(query, row)
        records=cur.fetchall()
        
        AllSubjects=[]
        
        for record in records:
            sn=SemesterSubject()
            sn.SemesterSubjectID=record[0]
            sn.SubjectID=record[1]
            
            AllSubjects.append(sn)
            
        return AllSubjects
    
    def UpdateMarksForm(self, rid, sessid, marks):
        cur=self.con.cursor()
        query="Update Marks set Marks=? where RegistrationID=? and SemesterSubjectID=?"
        row=(marks, rid, sessid)
        
        cur.execute(query, row)
        self.con.commit()
    
    
    
    
