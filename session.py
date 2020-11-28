import tkinter as tk 
from components import Session
from datalayer import DBSession
from tkinter import messagebox


class FrmSession:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
       
        self.Session=tk.StringVar()
        
        self.root.geometry("300x300")
        self.root.title("college sessions")
        
        self.lbl1=tk.Label(self.root, text="Enter Session")
        self.lbl1.pack()
        
        self.ent1=tk.Entry(self.root, textvariable=self.Session)
        self.ent1.pack()
        
        
        self.btn1=tk.Button(self.root, text="Add", command=self.AddButton)
        self.btn1.pack()
        
        
        self.root.mainloop()
        
    def AddButton(self):
        s=Session()
        s.Session=self.Session.get()
        db = DBSession()
        db.AddSession(s)
    
    def ShowDialog(self):
        self.root.mainloop()
    
        
        
        
        