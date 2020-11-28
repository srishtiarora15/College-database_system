import tkinter as tk 
from tkinter.ttk import Combobox 
from tkinter.ttk import Treeview 
from datalayer import DBSession
from datalayer import DALCourses
from datalayer import DBStudent
from datalayer import DBMarks
from marksform import AddMark


class Marks:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.geometry("1000x500")
        self.root.title("Student Marks")
        
        self.SessionID=tk.StringVar()
        self.CourseID=tk.StringVar()
        self.Semester=tk.StringVar()
        
        self.lbl1=tk.Label(self.root, text="Session")
        self.lbl1.pack()
        
        self.cmb1=Combobox(self.root, state="readonly")
        self.cmb1.pack()
        
        self.lbl2=tk.Label(self.root, text="Course")
        self.lbl2.pack()
        
        self.cmb2=Combobox(self.root, state="readonly")
        self.cmb2.pack()
        
        self.lbl3=tk.Label(self.root, text="Semester")
        self.lbl3.pack()
        
        self.cmb3=Combobox(self.root, state="readonly")
        self.cmb3.pack()
        
        self.btn1=tk.Button(self.root, text="Show", command=self.ShowClicked)
        self.btn1.pack()
        
        objDAL=DBSession()
        self.AllSessions=objDAL.GetSession()
        
        list1=[]
        
        for ses in self.AllSessions:
            list1.append(ses.Session)
            
        objDAL=DALCourses()
        self.ALLCourses=objDAL.GetCourses()
        
        list2=[]
        
        for pro in self.ALLCourses:
            list2.append(pro.CourseName)
        
        list3=[1, 2, 3, 4, 5, 6, 7,  8]
        
        self.cmb1['values']=list1
        self.cmb2['values']=list2
        self.cmb3['values']=list3
        
        
        
        
    def ShowClicked(self):
        self.tree1=Treeview(self.root)
        self.tree1.pack()
        
        self.tree1['columns']=("c1", "c2", "c3")
        self.tree1.heading("c1", text="RegistrationID")
        self.tree1.heading("c2", text="Name")
        self.tree1.heading("c3", text="RollNo")
        
        sessid=self.AllSessions[self.cmb1.current()].SessionID
        cid=self.ALLCourses[self.cmb2.current()].CourseID
        sem=self.cmb3.get()
        
        
        objDAL=DBStudent()
        AllDetails=objDAL.ViewStudent(sessid, cid, sem)
        
        i=0
        for stu in AllDetails:
            self.tree1.insert ("", i, text=stu.RegistrationID, 
                               values=(stu.RegistrationID, stu.Name, stu.RollNo))
            
            i+=1
        
        self.btn2=tk.Button(self.root, text="Marks", command=self.AddMarksClicked)
        self.btn2.pack()
        
        
    def AddMarksClicked(self):
        key=self.tree1.focus()
        SessionID=self.AllSessions[self.cmb1.current()].SessionID
        CourseID=self.ALLCourses[self.cmb2.current()].CourseID
        semester=self.cmb3.get()
        rid=self.tree1.item(key, "text")
        name=(self.tree1.item(key, "values"))[1]
        print(name)
        obj=AddMark(rid, SessionID, CourseID, name, semester)        
        
    def MarksClicked(self):
        key = self.tree1.focus()
        regid=int(self.tree1.item(key, 'text'))
        name =self.tree1(key, "values")[0]
        
        sessid=self.AllSessions[self.cmb1.current()].SessionID
        cid=self.ALLCourses[self.cmb2.current()].CourseID
        sem=self.cmb3.get()
        
        db=DBMarks()
        MarksList=db.AddMarks(regid)
        
        if MarksList !=[]:
            obj=AddMark(regid, sessid, cid, sem, name, MarksList)
            obj.UpdateMarksForm(regid, sessid, cid, sem, name, MarksList)
            obj.ShowDialog()
            
           # obj=UpdateMarksForm(regid, sessid, cid, sem, name, MarksList)
            #obj.ShowDialog()
            
        else:
            obj=AddMark()
            obj.MarksForm( regid, cid,name,sem)
            obj.ShowDialog()
            #obj=MarksForm(regid, sessid, sem, name)
            #obj.ShowDialog()
    
        
        