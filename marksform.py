import tkinter as tk 
#from components import Marks
from datalayer import DBMarks 


class AddMark:
    def __init__(self, rid, CourseID, SessionID, name, semester):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.geometry("500x500")
        self.root.title("Marks Form")
        self.y1=100
        self.y2=100
        
        self.RegistrationID=tk.StringVar()
        self.Name=tk.StringVar()
        
        self.lbl1=tk.Label(self.root, text="RegistrationID")
        self.lbl1.pack()
        
        self.ent1=tk.Entry(self.root, textvariable=self.RegistrationID)
        self.ent1.pack()
        
        self.RegistrationID.set(rid)
        self.Name.set(name)
        
        self.btn1=tk.Button(self.root, text="SAVE", command=self.Save)
        self.btn1.pack()
        
        objDAL=DBMarks()
        self.AllSubjects=objDAL.GetSubjects(SessionID, CourseID, semester)
        print(self.AllSubjects)
        self.AllMarks=[]
        
        for c in self.AllSubjects:
            e=tk.StringVar()
            self.AllMarks.append((e, c.SemesterSubjectID))
            self.lbl1=tk.Label(self.root, text=c.SubjectID)
            self.lbl1.place(x=50, y=self.y1)
            self.y1+=40
            
            self.ent=tk.Entry(self.root, textvariable=e)
            self.ent.place(x=130, y=self.y2)
            
            self.y2+=40
            
            
    def Save(self):
        
        for marks in self.AllMarks:
            mark = marks[0].get()
           
            SemesterSubjectID=marks[1]
            rid=int(self.RegistrationID.get())
            objDAL=DBMarks()
            objDAL.AddMarks(mark, SemesterSubjectID, rid)
            
        self.root.mainloop()
        
        
        
    def ShowDialog(self):
        self.root.mainloop()
        
        
        
            
            
        
        