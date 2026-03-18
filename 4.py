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
    def total(self):
        return sum(self.marks)
    def result(self):
        avg_marks=self.avg()
        if avg_marks>=90:
            return "A"
        elif avg_marks>=80:
            return "B"
        elif avg_marks  >=70:
            return "C"
        elif avg_marks>=60:
            return "D"
        else:
            return "F"
    def display(self):
        result=self.result()
        total=self.total()
        avg=self.avg()
        print(f"Name:{self.name} \n Result:{result} \n Average:{avg} \n Total:{total}")
        for sub,marks in zip(self.subjects,self.marks):
            print(f"{sub}: {marks}")
        print(f"Highest marks:{max(self.marks)} in {self.subjects[self.marks.index(max(self.marks))]}")
        print(f"Lowest marks:{min(self.marks)} in {self.subjects[self.marks.index(min(self.marks))]}")
s1=Student("Vaishu",[85,92,78],["Python","Science","Cloud Computing"])
s2=Student("Ravi",[37,65,48],["Maths","OOPS","English"])
s3=Student("Priya",[90,95,88],["Computer Networks","Science","Java"])
s1.display()
s2.display()
s3.display()
