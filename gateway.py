import tkinter as tk 
from AddCourse import FrmAdd
from Viewcourses import FrmView 
from session import FrmSession
from viewsession import ViewSessions
from Subject import FrmSubject
from viewsubject import ViewSubject 
from Student import FrmStudent
from viewstudent import ViewStudent
from AddSemesterSubject import AddSemesterSubject
from Enrollment import FrmEnrollment
from Marks import Marks
from DisplayStudentForm import DisplayStudentForm

class Gateway:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("500x500")
        self.root.title("College Database")
        
        self.btn1=tk.Button(self.root, text="AddCourse", command=self.Addclicked)
        self.btn1.place(x=50, y=50)
        
        self.btn2=tk.Button(self.root, text="ViewCourses", command=self.Viewclicked)
        self.btn2.place(x=150, y=50)
        
        self.btn3=tk.Button(self.root, text="AddSession", command=self.SessionsClicked)
        self.btn3.place(x=50, y=100)
        
        self.btn4=tk.Button(self.root, text="ViewSessions", command=self.ViewSessionsClicked)
        self.btn4.place(x=150, y=100)
        
        self.btn5=tk.Button(self.root, text="AddSubject", command=self.AddSubjectClicked)
        self.btn5.place(x=50, y=150)
        
        self.btn6=tk.Button(self.root, text="ViewSubject", command=self.ViewSubjectClicked)
        self.btn6.place(x=150, y=150)
        
        self.btn7=tk.Button(self.root, text="Register", command=self.RegisterClicked)
        self.btn7.place(x=50, y=200)
        
        self.btn8=tk.Button(self.root, text="View Student", command=self.ViewStudentClicked)
        self.btn8.place(x=150, y=200)
        
        self.btn9=tk.Button(self.root, text="AddSemesterSubject", command=self.AddSemesterSubClicked)
        self.btn9.place(x=50, y=250)
        
        self.btn10=tk.Button(self.root, text="Enrollment", command=self.EnrollmentClicked)
        self.btn10.place(x=50, y=300)
        
        self.btn11=tk.Button(self.root, text="Academic details", command=self.AcademicDetailsClicked)
        self.btn11.place(x=200, y=300)
        
        self.btn12=tk.Button(self.root, text="Display Student", command=self.DisplayStudentClicked)
        self.btn12.place(x=50, y=350)
       
        
        
        
        self.root.mainloop()
        
        
        
    def Addclicked(self):
        obj=FrmAdd()
    
    def Viewclicked(self):
        obj=FrmView()
        
    def SessionsClicked(self):
        obj=FrmSession()
    
    def ViewSessionsClicked(self):
        obj=ViewSessions()
        
    def AddSubjectClicked(self):
        obj=FrmSubject()
        
    def ViewSubjectClicked(self):
        obj=ViewSubject()
        
    def RegisterClicked(self):
        obj=FrmStudent()
        
    def ViewStudentClicked(self):
        obj=ViewStudent()
        
    def AddSemesterSubClicked(self):
        obj=AddSemesterSubject()
        
    def EnrollmentClicked(self):
        obj=FrmEnrollment()
        
    def AcademicDetailsClicked(self):
        obj=Marks()
        
    def DisplayStudentClicked(self):
        obj=DisplayStudentForm()
    
            
obj=Gateway()