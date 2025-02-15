class Student:
    college_name = "VIT"
    def __init__(self,name,department):
        self.name=name
        self.department=department
    def welcome(self):
        print("welcome to",self.college_name,self.name,"in",self.department)

s1=Student("vaibhav","CS")
s1.welcome()