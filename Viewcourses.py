import tkinter as tk 
from tkinter.ttk import Treeview
from datalayer import DALCourses
from tkinter import messagebox 

class FrmView:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.tree1=Treeview(self.root)
        self.tree1.pack()
        
        self.tree1['columns']=("c1", "c2")
        self.tree1.heading("c1", text="Course name")
        self.tree1.heading("c2", text="Description")
        
        objDAL=DALCourses()
        AllCourses=objDAL.GetCourses()
        
        i=0
        
        for pro in AllCourses:
            self.tree1.insert("",i, text=pro.CourseID,\
                              values=(pro.CourseName, pro.Description))
            i+=1
            
        
        
        
        self.btn1=tk.Button(self.root, text="Delete", command=self.Deleteclicked)
        self.btn1.pack()
         
        self.root.mainloop()
        
        
        
    def Deleteclicked(self):
        ret=messagebox.askyesno("College Database", "Do you want to delete the course")
        
        
        if ret==True:
            key =self.tree1.focus()

            CID = int( self.tree1.item(key,"text") )
            
            objDAL = DALCourses()
            objDAL.DeleteCourse(CID)
            
            self.tree1.delete(key)
            
        
        