import tkinter as tk 
from components import Student
from tkinter import messagebox 
from datalayer import DBStudent 
from tkinter.ttk import Combobox
from datalayer import DALCourses 
from datalayer import DBSession

class FrmStudent:
    def __init__(self):
       self.root=tk.Toplevel()
       self.root.grab_set()
       
       self.root.geometry("500x700")
       self.root.title("Student details")
       
       self.RollNo=tk.StringVar()
       self.Date=tk.StringVar()
       self.Name=tk.StringVar()
       self.DOB=tk.StringVar()
       self.Gender=tk.StringVar()
       self.FatherName=tk.StringVar()
       self.MotherName=tk.StringVar()
       self.Address=tk.StringVar()
       self.City=tk.StringVar()
       self.Nationality=tk.StringVar()
       self.ContactNo=tk.StringVar()
       self.EmailID=tk.StringVar()
       
       
       
       self.lbl2=tk.Label(self.root, text="RollNo")
       self.lbl2.place(x=50, y=50)
       
       self.ent2=tk.Entry(self.root, textvariable=self.RollNo)
       self.ent2.place(x=200, y=50)
       
       self.lbl3=tk.Label(self.root, text="Date")
       self.lbl3.place(x=50, y=80)
       
       self.ent3=tk.Entry(self.root, textvariable=self.Date)
       self.ent3.place(x=200, y=80)
       
       self.lbl4=tk.Label(self.root, text="Name")
       self.lbl4.place(x=50, y=110)
       
       self.ent4=tk.Entry(self.root, textvariable=self.Name)
       self.ent4.place(x=200, y=110)
       
       self.lbl5=tk.Label(self.root, text="DOB")
       self.lbl5.place(x=50, y=140)
       
       self.ent5=tk.Entry(self.root, textvariable=self.DOB)
       self.ent5.place(x=200, y=140)
       
       self.lbl6=tk.Label(self.root, text="Gender")
       self.lbl6.place(x=50, y=170)
       
       self.radio1=tk.Radiobutton(self.root, text="Female", value=1)
       self.radio1.place(x=200, y=170)

       self.radio2=tk.Radiobutton(self.root, text="Male", value=2)
       self.radio2.place(x=200, y=190)
       
       self.lbl7=tk.Label(self.root, text="FatherName")
       self.lbl7.place(x=50, y=210)
       
       self.ent7=tk.Entry(self.root, textvariable=self.FatherName)
       self.ent7.place(x=200, y=210)
       
       self.lbl8=tk.Label(self.root, text="MotherName")
       self.lbl8.place(x=50, y=240)
       
       self.ent8=tk.Entry(self.root, textvariable=self.MotherName)
       self.ent8.place(x=200, y=240)
       
       self.lbl9=tk.Label(self.root, text="Address")
       self.lbl9.place(x=50, y=270)
       
       self.ent9=tk.Entry(self.root, textvariable=self.Address)
       self.ent9.place(x=200, y=270)
       
       self.lbl10=tk.Label(self.root, text="City")
       self.lbl10.place(x=50, y=300)
       
       self.ent10=tk.Entry(self.root, textvariable=self.City)
       self.ent10.place(x=200, y=300)
       
       self.lbl11=tk.Label(self.root, text="ContactNo")
       self.lbl11.place(x=50, y=330)
       
       self.ent11=tk.Entry(self.root, textvariable=self.ContactNo)
       self.ent11.place(x=200, y=330)
       
       self.lbl12=tk.Label(self.root, text="EmailID")
       self.lbl12.place(x=50, y=360)
       
       self.ent12=tk.Entry(self.root, textvariable=self.EmailID)
       self.ent12.place(x=200, y=360)
       
       self.lbl13=tk.Label(self.root, text="Nationality")
       self.lbl13.place(x=50, y=390)
       
       self.ent13=tk.Entry(self.root, textvariable=self.Nationality)
       self.ent13.place(x=200, y=390)
       
       self.lbl14=tk.Label(self.root, text="Course")
       self.lbl14.place(x=50, y=420)
       
       self.cmb1=Combobox(self.root, state="readonly")
       self.cmb1.place(x=200, y=420)
       
       self.lbl15=tk.Label(self.root, text="Session")
       self.lbl15.place(x=50, y=460)
       
       self.cmb2=Combobox(self.root, state="readonly")
       self.cmb2.place(x=200, y=460)
       
       self.btn1=tk.Button(self.root, text="Register", command=self.RegisterClicked)
       self.btn1.place(x=200, y=520)
       
       objDAL=DALCourses()
       self.AllCourses=objDAL.GetCourses()
       
       list1=[]
       
       for pro in self.AllCourses:
           list1.append(pro.CourseName)
           
       objDAL=DBSession() 
       self.AllSessions=objDAL.GetSession()
       
       list2=[]
       
       for ses in self.AllSessions:
           list2.append(ses.Session)
           
           
       self.cmb1['values']=list1 
       self.cmb2['values']=list2
       self.root.mainloop()
       
    def RegisterClicked(self):
        stu=Student()
        stu.RollNo=self.RollNo.get()
        stu.Date=self.Date.get()
        stu.Name=self.Name.get()
        stu.DOB=self.DOB.get()
        stu.Gender=self.Gender.get()
        stu.FatherName=self.FatherName.get()
        stu.MotherName=self.MotherName.get()
        stu.Address=self.Address.get()
        stu.Nationality=self.Nationality.get()
        stu.ContactNo=self.ContactNo.get()
        stu.EmailID=self.EmailID.get()
        
        
        index1=self.cmb1.current()
        stu.CourseID=self.AllCourses[index1].CourseID

        index2=self.cmb2.current()
        stu.SessionID=self.AllSessions[index2].SessionID

        objDAL=DBStudent()
        objDAL.AddStudent(stu)
        messagebox.showinfo("Register", "Registration Successful")
    
       
       
       

    