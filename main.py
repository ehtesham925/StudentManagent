# Student Management 
import random
import time 
# implemention inheritance in v4 

# College/Institute class(master)---> Student class (attributes/methods) ---> Course class (attributes/methods) ---> Person class 
# handle both Student & Course

# decorator 
def timer(func):
    def wrapper(*args):
        start = time.time()
        # time.sleep(1)
        res = func(*args)
        end = time.time()
        return {f"{func.__name__} ran for {end-start} time" }
    return wrapper


# what type of inheritance i can use ?
# College,Student,Course 
# tejaswi --> hie inheritance 
# pranav --> multilevel 
# aditya --> multilevel 

# dependencies 
"""   College(one) --> Students(many) ---> Course(many) ---> Person   (relationships)

types of relationships --
one to one (Single inheritance)
one to many (Hierarchical)
many to one (Multiple)
many to many (Hybrid)
"""


"""  
-----College(one)-----
        |
    Students(many)
        |
    Courses (many)

"""



# attributes 
# address, affilated_to, courses_provided
# methods (getters/setters)


# Multilevel inheritance 


# base class 
class College:
    College_name = "Govt College of Hyderabad" # class variable 
    def __init__(self,address,affilated_to, courses_provided:list):
        self.address = address
        self.affilated_to = affilated_to
        self.courses_provided = courses_provided
    
    @classmethod
    def get_college_name(cls):
        return cls.College_name

    # @staticmethod
    # def get_clg_name():
    #     return College.College_name

    # {, , , , []}
    # @timer
    def get_college_details(self):
        return {
            "college_name":College.College_name,
            "address":self.address, 
            "affilated_to": self.affilated_to,
             "courses provided": self.courses_provided
            }
    
    
# college-->student  # done   

# student is bind with a college 
# attributes -- name, rollno, age 
# methods (marks/grades)
# sub class 
class Student(College):
    def __init__(self, stuname, rollno, age,address,affilated_to, courses_provided):
        super().__init__(address,affilated_to, courses_provided)
        self.name = stuname 
        self.__rollno = rollno # private variable 
        self.age = age 
        self.grades = None

    def set_grade(self,grade:float):
        self.grades = grade 
    
    def get_grade(self):
        return self.grades
   
    def get_student_details(self):
        return {

            "student_details":
                {
                "name":self.name,
                "rollno":self.__rollno,
                "age": self.age,
                "grade":self.grades
                
           
        },
        "college_details": self.get_college_details()
        }
    


# student = Student("Alice",31,21,"Ameerpet","ou",['M.tech','B.tech'])
# print(student.get_college_details())



# course --> students 
class Course(Student):
    def __init__(self,name,max_students,stuname, rollno, age,address,affilated_to, courses_provided):
        super().__init__(stuname, rollno, age,address,affilated_to, courses_provided)
        self.course_name = name 
        self.max_students = max_students
        self.students = []

    
    def add_student(self,student):
        if len(self.students)<(self.max_students):
            self.students.append(student)
            return True
        return False 
    
   
    def get_average_grade(self):
        value = 0 
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
    
    def get_details(self):
        lst = []
        for student in self.students:
            lst.append(student.get_student_details())
        return lst 

    def get_course_details(self):
        return {
            "course_details":{
            "course_name":self.course_name,
            "max_students":self.max_students,
        },
        "student_details":self.get_student_details()
        }
    

