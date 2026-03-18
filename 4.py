""" class student:
    name="vaishu"
    age=21
s1=student()
print(s1.name)
print(s1.age)

class Book:
    title="Harry Potter"
    author="J.K. Rowling"
    price=350 
    
b1=Book()
print(b1.title)

class Student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
s1=Student("Vaishu",21,101)
s2=Student("Ravi",22,102)
s3=Student("Priya",20,103)
print(s1.name,s2.age,s3.rollno)"""

class Student:
    def __init__(self,name,marks,subjects):
        self.name=name
        self.marks=marks
        self.subjects=subjects
    def avg(self):
        return sum(self.marks)/len(self.marks)
    def sum(self):
        return sum(self.marks)
    def result(self):
        if self.avg()>=90:
            return "A"
        elif self.avg()>=80:
            return "B"
        elif self.avg()>=70:
            return "C"
        elif self.avg()>=60:
            return "D"
        else:
            return "F"
    def display(self):
        print(f"Name:{self.name} \n Marks in {self.subjects}:{self.marks} \n Result:{self.result()} \n Average:{self.avg()} \n Total:{self.sum()}")
s1=Student("Vaishu",[85,92,78],["Python","Science","Cloud Computing"])
s2=Student("Ravi",[37,65,48],["Maths","OOPS","English"])
s3=Student("Priya",[90,95,88],["Computer Networks","Science","Java"])
s1.display()
s2.display()
s3.display()
