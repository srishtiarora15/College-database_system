import tkinter as tk 
from datalayer import DBMarks 

class UpdateMarksForm:
    def __init__(self, regid, sessid, cid, sem, name, Marks):
        self.root=tk.Toplevel()
        self.root.geometry("500x500")
        self.root.title("Marks")
        
        self.regid=regid
        self.y=130
        self.reg=tk.StringVar()
        self.name=tk.StringVar()
        
        self.lbl1=tk.Label(self.root, text="RegistrationID")
        self.lbl1.place(x=40, y=40)
        self.ent1=tk.Entry(self.root, textvariable=self.reg, state="readonly")
        self.ent1.place(x=140, y=40)
        self.reg.set(self.regid)
        
        self.lbl3=tk.Label(self.root, text="Name")
        self.lbl3.place(x=300, y=40)
        self.ent2=tk.Entry(self.root, textvariable=self.name, state="readonly")
        self.ent2.place(x=400, y=40)
        self.name.set(name)
        
        self.lbl5=tk.Label(self.root, text="Subject")
        self.lbl5.place(x=40, y=100)
        self.lbl6=tk.Label(self.root, text="Marks")
        self.lbl6.place(x=180, y=100)
        
        dbsubjects=DBMarks()
        self.AllSubjects=dbsubjects.GetSubjects(sessid, cid, sem)
        self.MarksList=[]
        
        for a,m in zip(self.AllSubjects, Marks):
            listvar=tk.StringVar()
            self.MarksList.append((listvar, a.SemesterSubjectID))
            lbl4=tk.Label(self.root, text=a.Subject)
            lbl4.place(x=45, y=self.y)
            ent3=tk.Entry(self.root, textvariable=listvar)
            ent3.place(x=140, y=self.y)
            self.y+=40
            listvar.set(m)
            
            
        self.btn1=tk.Button(self.root, text="Update", command=self.UpdateMarks)
        self.btn1.place(x=100, y=self.y+50)
     
        
        
    def UpdateMarks(self):
        db=DBMarks()
        for marks in self.MarksList:
            mark=marks[0].get()
            ssid=marks[1]
            regid=self.regid
            
            db.UpdateMarksForm(regid, ssid, mark)
            
        
            
            
    def showdialog(self):
        self.root.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        