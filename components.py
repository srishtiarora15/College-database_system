class Course:
    def __init__(self):
        self.CourseID = 0
        self.CourseName = ""
        self.Description = ""
        
        
class Session:
    def __init__(self):
        self.SessionID=0
        self.Session=""


class Subject:
    def __init__(self):
        self.SubjectID=0
        self.SubjectName=""
        self.Description=""
        
class Student:
    def __init__(self):
        self.RegistrationID=0
        self.RollNo=0
        self.Date=0
        self.Name=""
        self.DOB=0
        self.Gender=""
        self.FatherName=""
        self.MotherName=""
        self.Address=""
        self.City=""
        self.ContactNo=0
        self.EmailID=""
        self.Nationality=""
        self.CourseID=""
        self.SessionID=""
        
class SemesterSubject:
    def __init__(self):
        self.SemesterSubjectID=0
        self.SessionID=""
        self.CourseID=""
        self.Semester=0
        self.SubjectID=""
        
class Enrollment:
    def __init__(self):
        self.EnrollmentID=0
        self.Date=""
        self.Semester=0
        self.RegistrationID=0
        self.IsCurrent=0
