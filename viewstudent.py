import tkinter as tk
from tkinter.ttk import Treeview 
from datalayer import DBStudent 
from tkinter import messagebox 

class ViewStudent:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.title("Student Details")
        self.tree1=Treeview(self.root)
        self.tree1.pack()
        
        self.tree1['columns']=("c1", "c2", "c3", "c4")
        self.tree1.heading("c1", text="RollNo")
        self.tree1.heading("c2", text="Name")
        self.tree1.heading("c3", text="CourseID")
        self.tree1.heading("c4", text="SessionID")
        
        objDAL=DBStudent()
        AllStudents=objDAL.GetStudent()
        
        i=0
        
        for stu in AllStudents:
            self.tree1.insert("", i, text=stu.RegistrationID, 
                              values=(stu.RollNo, stu.Name, stu.CourseID, stu.SessionID))
            
            i+=1
            
        self.btn1=tk.Button(self.root, text="Delete", command=self.DeleteClicked)
        self.btn1.pack()
        
        
    def DeleteClicked(self) :
           ret=messagebox.askyesno("Registration", "Do you want to delete the data?")
        
        
           if ret==True:
                key =self.tree1.focus()

                SID = int( self.tree1.item(key,"text") )
            
                objDAL = DBStudent()
                objDAL.DeleteStudent(SID)
                
                self.tree1.delete(key)
    