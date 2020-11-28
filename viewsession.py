import tkinter as tk
from tkinter.ttk import Treeview 
from tkinter import messagebox
from datalayer import DBSession
from components import Session

class ViewSessions:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.tree=Treeview(self.root)
        self.tree.pack()
        
        self.tree['columns']=("c1")
        self.tree.heading("c1", text="Session")
        
        db=DBSession()
        AllSessions=db.GetSession()
        
        i=1
        
        for c in AllSessions:
            self.tree.insert("", i, text=c.SessionID, values=(c.Session))
            i=i+1
            
            
        self.btn=tk.Button(self.root, text="Delete", command=self.delete)
        self.btn.pack()
        
    def delete(self):
        ret=messagebox.askyesno("Session", "do you want to delete Session?")
        if ret==True:
            key=self.tree.focus()
            cid=int(self.tree.item(key, "text"))
            c=Session()
            c.SessionID=cid
            db=DBSession()
            db.DeleteSession(c)
            self.tree.delete(key)