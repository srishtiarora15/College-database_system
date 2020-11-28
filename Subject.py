import tkinter as tk 
from datalayer import DBSubject
from components import Subject
from tkinter import messagebox 

class FrmSubject:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.geometry("400x400")
        self.root.title("Add Subject")
        
        self.SubjectName=tk.StringVar()
        self.Description=tk.StringVar()
        
        
        self.lbl1=tk.Label(self.root, text="Subject Name")
        self.lbl1.place(x=50, y=50)
        
        self.ent1=tk.Entry(self.root, textvariable=self.SubjectName)
        self.ent1.place(x=150, y=50)
           
        self.lbl2=tk.Label(self.root, text="Description")
        self.lbl2.place(x=50, y=150)
        
        self.ent2=tk.Entry(self.root, textvariable=self.Description)
        self.ent2.place(x=150, y=150)
        
        self.btn1=tk.Button(self.root, text="save", command=self.SaveClicked)
        self.btn1.place(x=180, y=180)
        
    def SaveClicked(self):
            p=Subject()
            
            p.SubjectName=self.SubjectName.get()
            p.Description=self.Description.get()
            obj=DBSubject()
            obj.AddSubject(p)
            
            messagebox.showinfo("AddSubject", "Subject has been added successfully")
     
        
       
        
        
        