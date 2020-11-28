import tkinter as tk
from tkinter.ttk import Combobox
from datalayer import DBMarks
from functools import partial

class ViewMarksForm:
    def __init__(self, sem, regid, name, sessid, cid, Marks):
        self.root=tk.Toplevel()
        self.root.geometry("500x500")
        self.root.title("Marks")
        self.y=5
        self.rid=tk.StringVar()
        self.name=tk.StringVar()
        
        self.lbl2=tk.Label(self.root, text="RegistrationID")
        self.lbl2.place(x=10, y=10)
        self.ent2=tk.Entry(self.root, textvariable=self.rid, state="readonly")
        self.ent2.place(x=110, y=10)
        self.rid.set(regid)
        
        self.lbl3=tk.Label(self.root, text="Name")
        self.lbl3.place(x=250, y=10)
        self.ent3=tk.Entry(self.root, textvariable=self.name, state="readonly")
        self.ent3.place(x=250, y=10)
        self.name.set(name)
        
        self.lbl1=tk.Label(self.root, text="Semester")
        self.lbl1.place(x=10, y=50)
        self.cmb = Combobox(self.root)
        self.cmb.place(x=110, y=50)
        self.cmb['values']=["1", "2", "3", "4", "5", "6", "7", "8"]
        
        self.btn1=tk.Button(self.root, text="Show", command=partial(self.ShowClicked, sessid, cid, regid))
        self.btn1.place(x=350, y=50)
        
        self.frame=tk.Frame(self.root, width=400, height=400)
        self.frame.place(x=10, y=300)
        
        self.GetMarks(sessid, cid, sem, Marks)
        
        
    def ShowClicked(self, sessid, cid, regid):
        self.y=5
        self.frame.destroy()
        self.frame=tk.Frame(self.root)
        self.frame.place(x=45, y=100)
        sem=self.cmb.get()
        db=DBMarks()
        Marks=db.CheckMarks(regid, sem)
        self.GetMarks(sessid, cid, sem, Marks)
       
        
        
    def GetMarks(self, sessid, cid, sem, Marks):
        db=DBMarks()
        self.AllSubjects=db.GetSubjects(sessid, cid, sem)
        self.MarksList=[]
        
        if Marks==[]:
            Marks = ["NULL"]*len(self.AllSubjects)
            
        for a,m in zip(self.AllSubjects,Marks):
            listvar=tk.StringVar()
            self.MarksList.append(listvar, a.SemesterSubjectID)
            lbl=tk.Label(self.frame, text=a.Subject)
            lbl.place(x=95, y=self.y)
            ent=tk.Entry(self.frame, textvariable=listvar, state="readonly")
            ent.place(x=95, y=self.y)
            self.y+=40
            listvar.set(m)
            
            
    def showdialog(self):
        self.root.mainloop()