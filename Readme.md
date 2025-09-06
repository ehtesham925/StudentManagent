# Student Management Program 


 
### implemention inheritance in v4 

College/Institute class(master)---> Student class (attributes/methods) ---> Course class (attributes/methods) ---> Person class 
 handle both Student & Course


what type of inheritance i can use ?
College,Student,Course 
tejaswi --> hie inheritance 
pranav --> multilevel 
aditya --> multilevel 



### dependencies 
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


attributes 
address, affilated_to, courses_provided
methods (getters/setters)


### Multilevel inheritance 


    
college-->student  # done   
student is bind with a college 
attributes -- name, rollno, age 
methods (marks/grades)
