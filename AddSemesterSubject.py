import tkinter as tk 
from components import SemesterSubject
from tkinter import messagebox 
from datalayer import DBSubject
from tkinter.ttk import Combobox
from datalayer import DBStudent
from datalayer import DALCourses
from datalayer import DBSession
from tkinter.ttk import Treeview



class AddSemesterSubject:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.geometry("1000x1000")
        self.root.title("AddSemesterSubject")
        
        self.SessionID=tk.StringVar()
        self.CourseID=tk.StringVar()
        self.Semester=tk.StringVar()
        self.SubjectID=tk.StringVar()
        
        self.lbl1=tk.Label(self.root, text="Session")
        self.lbl1.place(x=50, y=50)
        
        self.cmb1=Combobox(self.root, state="readonly")
        self.cmb1.place(x=150, y=50)
        
        self.lbl2=tk.Label(self.root, text="Course")
        self.lbl2.place(x=50, y=100)
        
        self.cmb2=Combobox(self.root, state="readonly")
        self.cmb2.place(x=150, y=100)
        
        self.lbl3=tk.Label(self.root, text="Semester")
        self.lbl3.place(x=50, y=150)
        
        self.cmb3=Combobox(self.root, state="readonly")
        self.cmb3.place(x=150, y=150)
        
        self.lbl4=tk.Label(self.root, text="Subject")
        self.lbl4.place(x=50, y=200)
        
        self.cmb4=Combobox(self.root, state="readonly")
        self.cmb4.place(x=150, y=200)
        
        self.btn1=tk.Button(self.root, text="Add", command=self.AddClicked)
        self.btn1.place(x=70, y=250)
        
        self.btn2=tk.Button(self.root, text="Show", command=self.ShowClicked)
        self.btn2.place(x=120, y=250)
        
        objDAL=DBSession()
        self.AllSessions=objDAL.GetSession()
        
        list1=[]
        
        for ses in self.AllSessions:
           list1.append(ses.Session)
           
           
        objDAL=DALCourses()
        self.AllCourses=objDAL.GetCourses()
        
        list2=[]
        
        for pro in self.AllCourses:
            list2.append(pro.CourseName)
            
        list3=[1,2, 3, 4, 5, 6, 7, 8]
            
        objDAL=DBSubject()
        self.AllSubjects=objDAL.GetSubject()
        
        list4=[]
        
        for sub in self.AllSubjects:
            list4.append(sub.SubjectName)
            
            
        self.cmb1['values']=list1
        self.cmb2['values']=list2
        self.cmb3['values']=list3
        self.cmb4['values']=list4
        
        
        
    def AddClicked(self):
        sem=SemesterSubject()
        sem.SessionID=self.SessionID.get()
        sem.CourseID=self.CourseID.get()
        sem.Semester=self.Semester.get()
        sem.SubjectID=self.SubjectID.get()
        
        
        index1=self.cmb1.current()
        sem.SessionID=self.AllSessions[index1].SessionID

        index2=self.cmb2.current()
        sem.CourseID=self.AllCourses[index2].CourseID
        
        sem.Semester=self.cmb3.get()
        
        index4=self.cmb4.current()
        sem.SubjectID=self.AllSubjects[index4].SubjectID

        objDAL=DBSubject()
        objDAL.AddSemesterSubject(sem)
        messagebox.showinfo("SemesterSubject", "Subject Added Successfully")
        
        
    def ShowClicked(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.title("Course Details")
        
        self.tree1=Treeview(self.root)
        self.tree1.pack()
        
        self.tree1['columns']=["c1", "c2", "c3", "c4"]
        self.tree1.heading("c1", text="Session")
        self.tree1.heading("c2", text="Course")
        self.tree1.heading("c3", text="Semester")
        self.tree1.heading("c4", text="Subject")
        
        objDAL=DBSubject()
        AllSemesterSubjects=objDAL.GetSemesterSubject()
        
        i=0
        
        for sem in AllSemesterSubjects:
            self.tree1.insert("", i, text=sem.SemesterSubjectID, 
                              values=(sem.SessionID, sem.CourseID, sem.Semester, sem.SubjectID))
            
            i+=1
            
        self.btn3=tk.Button(self.root, text="Delete", command=self.DeleteClicked)
        self.btn3.pack()
        
    def DeleteClicked(self):
        ret=messagebox.askyesno("Course Deteils", "Do you want to delete SemesterSubject")
            
        if ret==True:
            key=self.tree1.focus()
                
            semid=int(self.tree1.item(key, "text"))
                
            DAL=DBSubject()
            DAL.DeleteSemesterSubject(semid)
            self.tree1.delete(key)
                
        
        
        
        
        
        
        
        
        