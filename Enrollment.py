import tkinter as tk
from components import Enrollment
from datalayer import DALEnrollment
from datalayer import DBStudent
from tkinter import messagebox 
from tkinter.ttk import Combobox
from datetime import date 


class FrmEnrollment:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.geometry("400x400")
        self.root.title("Enrollment")
        
        self.RollNo=tk.StringVar()
        self.Name=tk.StringVar()
        self.RegistrationID=tk.StringVar()
        self.Gender=tk.StringVar()
        self.FatherName=tk.StringVar()
        self.MotherName=tk.StringVar()
        
        self.lbl1=tk.Label(self.root, text="RollNo",)
        self.lbl1.place(x=50, y=50)
        
        self.ent1=tk.Entry(self.root, textvariable=self.RollNo)
        self.ent1.place(x=200, y=50)
        
        self.btn1=tk.Button(self.root, text="Find", command=self.FindClicked)
        self.btn1.place(x=350, y=50)
        
        self.lbl2=tk.Label(self.root, text="Name")
        self.lbl2.place(x=50, y=100)
        
        self.ent2=tk.Entry(self.root, textvariable=self.Name, state="readonly")
        self.ent2.place(x=200, y=100)
        
        self.lbl3=tk.Label(self.root, text="RegistrationID")
        self.lbl3.place(x=50, y=150)
        
        self.ent3=tk.Entry(self.root, textvariable=self.RegistrationID, state="readonly")
        self.ent3.place(x=200, y=150)
        
        self.lbl6=tk.Label(self.root, text="Father Name")
        self.lbl6.place(x=50, y=200)
        
        self.ent6=tk.Entry(self.root, textvariable=self.FatherName, state="readonly")
        self.ent6.place(x=200, y=200)
        
        self.lbl7=tk.Label(self.root, text="MotherName",)
        self.lbl7.place(x=50, y=250)
        
        self.ent7=tk.Entry(self.root, textvariable=self.MotherName, state="readonly")
        self.ent7.place(x=200, y=250)
        
        self.btn2=tk.Button(self.root, text="Register", command=self.RegisterClicked)
        self.btn2.place(x=80, y=350)
        
        self.cmb1=Combobox(self.root, state="readonly")
        self.cmb1.place(x=80, y=300)
        
        list1=[1, 2, 3, 4, 5, 6, 7, 8]
        self.cmb1['values']=list1
        
    def FindClicked(self):
        
        objDAL = DBStudent()
       # AllStudents= objDAL.FindStudent(int(self.RollNo.get()))
        AllStudents=objDAL.FindStudent(int(self.ent1.get()))
        for all in AllStudents:
            self.RegistrationID.set(all.RegistrationID)
            self.Name.set(all.Name)
            self.FatherName.set(all.FatherName)
            self.MotherName.set(all.MotherName)
            
    def RegisterClicked(self):
        
        en=Enrollment()
        en.Semester=self.cmb1.get()
        en.RegistrationID=int(self.RegistrationID.get())
        today=date.today()
        en.Date=str(today)
        
        objDAL=DALEnrollment()
        objDAL.AddEnrollment(en)
        
       
        
        messagebox.showinfo("Registration", "Registration successful")
            
        