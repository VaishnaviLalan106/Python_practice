
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
while True:
    print('''Options:\n
              1. Add Student \n
              2. View Student\n
              3. Update Student\n
              4. Exit''')
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter name:")
        marks=list(map(int,input("Enter marks:").split()))
        subjects=list(map(str,input("Enter subjects:").split()))
        s1=Student(name,marks,subjects)
        s1.display()
    elif choice==2:
        s1.display()
    elif choice==3:
        name=input("Enter name:")
        marks=list(map(int,input("Enter marks:").split()))
        subjects=list(map(str,input("Enter subjects:").split()))
        s1=Student(name,marks,subjects)
        s1.display()
    elif choice==4:
        print("Byee")
        break