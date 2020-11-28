import tkinter as tk 
from datalayer import DALCourses 
from components import Course

class FrmAdd:
    def __init__(self):
        
        self.root=tk.Toplevel()
        self.root.grab_set()
    
        self.CourseName=tk.StringVar()
        self.Description=tk.StringVar()
    
        self.root.geometry("300x300")
        self.root.title("College Database")
    
        self.lbl1=tk.Label(self.root, text="Course Name")
        self.lbl1.place(x=30, y=30)
            
        self.ent1=tk.Entry(self.root, textvariable=self.CourseName)
        self.ent1.place(x=150, y=30)
    
        self.lbl2=tk.Label(self.root, text="Description")
        self.lbl2.place(x=30, y= 60)
        
        self.ent2=tk.Entry(self.root, textvariable=self.Description)
        self.ent2.place(x=150, y=60)
        
        self.btn1=tk.Button(self.root, text="save", command=self.saveclicked)
        self.btn1.place(x=60, y=150)
        
        self.btn2=tk.Button(self.root, text="cancel", command=self.root.destroy)
        self.btn2.place(x=110, y=150)
        
        self.root.mainloop()
        
    def saveclicked(self):
        c=Course()
        c.CourseName=self.CourseName.get()
        c.Description=self.Description.get()
        
        
        objDAL=DALCourses()
        objDAL.AddCourses(c)
    
    