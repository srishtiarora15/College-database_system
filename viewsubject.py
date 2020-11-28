import tkinter as tk
from tkinter.ttk import Treeview 
from tkinter import messagebox 
from datalayer import DBSubject
from components import Subject

class ViewSubject:
    
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.tree=Treeview(self.root)
        self.tree.pack()
        
        self.tree['columns']=("c1", "c2")
        self.tree.heading("c1", text="Subject")
        self.tree.heading("c2", text="Description")
        
        db=DBSubject()
        AllSubjects=db.GetSubject()
        
        i=1
        
        for c in AllSubjects:
            self.tree.insert("", i, text=c.SubjectID, values=(c.SubjectName, c.Description))
            i=i+1
            
        self.DeleteButton=tk.Button(self.root, text="Delete", command=self.DeleteClicked)
        self.DeleteButton.pack()
        
        
    def DeleteClicked(self):
        ret=messagebox.askyesno("Courses", "do you want to delete the subject?")
        if ret==True:
            key=self.tree.focus()
            sid=int(self.tree.item(key, "text"))
            c=Subject()
            
            db=DBSubject()
            c.SubjectID=sid
            db.DeleteSubject(c)
            self.tree.delete(key)
            