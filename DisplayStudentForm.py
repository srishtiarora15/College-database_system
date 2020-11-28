import tkinter as tk 
from tkinter.ttk import Combobox, Treeview
from datalayer import DBSession, DALCourses, DBStudent, DBMarks 
from marksform import AddMark
from UpdateMarksForm import UpdateMarksForm
from viewmarksform import ViewMarksForm 

class DisplayStudentForm:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.geometry("800x300")
        self.root.title("Marks")
        
        self.lbl1=tk.Label(self.root, text="Session")
        self.lbl1.place(x=10, y=10)
        self.cmb1=Combobox(self.root, state="readonly")
        self.cmb1.place(x=70, y=10)
        dbsession=DBSession()
        self.AllSessions=dbsession.GetSession()
        SessionList=[]
        for sess in self.AllSessions:
            SessionList.append(sess.Session)
        self.cmb1['values']=SessionList
        
        self.lbl2=tk.Label(self.root, text="Course")
        self.lbl2.place(x=250, y=10)
        self.cmb2=Combobox(self.root, state="readonly")
        self.cmb2.place(x=310, y=10)
        dbcourse=DALCourses()
        self.AllCourses=dbcourse.GetCourses()
        CourseList=[]
        for cour in self.AllCourses:
            CourseList.append(cour.CourseName)
        self.cmb2['values']=CourseList
        
        self.lbl3=tk.Label(self.root, text="Semester")
        self.lbl3.place(x=490, y=10)
        self.cmb3=Combobox(self.root, state="readonly")
        self.cmb3.place(x=560, y=10)
        self.cmb3['values']=["1", "2", "3", "4", "5", "6", "7", "8"]
        
        self.btn1=tk.Button(self.root, text="Show", command=self.ShowClicked)
        self.btn1.place(x=750, y=10)
        
        self.Tree1=Treeview(self.root)
        self.Tree1.place(x=10, y=70)
        self.Tree1['columns']=['c1', 'c2', 'c3', 'c4', 'c5']
        self.Tree1.heading("#0", text="RegID")
        self.Tree1.heading("c1", text="Name")
        self.Tree1.heading("c2", text="RollNo")
        
        self.btn2=tk.Button(self.root, text="Marks", command=self.MarksClicked)
        self.btn2.place(x=300, y=310)
        
        self.btn3=tk.Button(self.root, text="View Marks", command=self.ViewMarksClicked)
        self.btn3.place(x=460, y=310)
        
    def ShowClicked(self):
        sessid=self.AllSessions[self.cmb1.current()].SessionID
        cid=self.AllCourses[self.cmb2.current()].CourseID
        sem=self.cmb3.get()
        
        db=DBStudent()
        AllDetails=db.ViewStudent(sessid, cid, sem)
        
        i=0
        for ad in AllDetails:
            self.Tree1.insert("", i, text=ad.RegistrationID, values=(ad.Name, ad.RollNo))
            i+=1
            
    def MarksClicked(self):
        key=self.Tree1.focus()
        regid=int(self.Tree1.item(key,'text'))
        name=self.Tree1.item(key, "values")[0]
        sessid=self.AllSessions[self.cmb1.current()].SessionID
        cid=self.AllCourses[self.cmb2.current()].CourseID
        sem=self.cmb3.get()
        
        db=DBMarks()
        MarksList=db.CheckMarks(regid, sem)
        
        if MarksList!=[]:
            obj=UpdateMarksForm(regid, sessid, cid, sem, name, MarksList)
            obj.showdialog()
            
        else:
            obj=AddMark(regid, sessid, cid, sem, name)
            obj.showdialog()
            
    def ViewMarksClicked(self):
        key=self.Tree1.focus()
        regid=int(self.Tree1.item(key, "text"))
        name=self.Tree1.item(key, "values")[0]
        
        sessid=self.AllSessions[self.cmb1.current()].SessionID
        cid=self.AllCourses[self.cmb2.current()].CourseID
        sem=self.cmb3.get()
        
        db=DBMarks()
        
        MarksList=db.CheckMarks(regid, sem)
        
        obj=ViewMarksForm(sem, regid, name, sessid, cid, MarksList)
        obj.showdialog()
        
    def showdialog(self):
        self.root.mainloop()
        
#obj=DisplayStudentForm()
#obj.showdialog()           
            
        
            