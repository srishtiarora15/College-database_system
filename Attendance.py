import tkinter as tk
from datalayer import DBStudent



class Attendance:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.geometry("500x500")
        self.root.title("Attendance")
        