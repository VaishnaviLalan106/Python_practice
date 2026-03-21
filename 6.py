import json 
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
    def save_students(students):
        data =[]
        for s in students:
            data.append({
              "name": s.name,
              "marks": s.marks,
              "subjects": s.subjects
            })
    
        with open("students.json", "w") as f:
           json.dump(data, f)
    def load_students():
        students = []
        try:
             with open("students.json", "r") as f:
                data = json.load(f)
            
                for item in data:
                    s = Student(item["name"], item["marks"], item["subjects"])
                    students.append(s)
        except:
            pass
        return students
""" s1=Student("Vaishu",[85,92,78],["Python","Science","Cloud Computing"])
s2=Student("Ravi",[37,65,48],["Maths","OOPS","English"])
s3=Student("Priya",[90,95,88],["Computer Networks","Science","Java"])
s1.display()
s2.display()
s3.display() """
students=Student.load_students()
while True:
    print('''Options:\n
              1. Add Student \n
              2. View Student\n
              3. Update Student\n
              4. Search Student\n
              5. Delete Student\n
              6. Exit''')
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter name:")
        marks=list(map(int,input("Enter marks:").split()))
        subjects=list(map(str,input("Enter subjects:").split()))
        s=Student(name,marks,subjects)
        students.append(s)
        Student.save_students(students)
    elif choice==2:
        for s in students:
            s.display()
        if not students:
            print("Students are misssinggg !!!")
    elif choice==3:
        search=input("Enter name to update:\n")
        found = False
        for s in students:
           if s.name.lower() == search.lower():
              s.marks = list(map(int, input("Enter new marks: ").split()))
              s.subjects = list(map(str, input("Enter new subjects: ").split()))
              print("Student updated")
              Student.save_students(students)
              found = True
              break
        if not found:
            print("Student not found")
    elif choice==4:
        found=False
        findddd=input("Enter the name to search:")
        for s in students:
            if s.name.lower()==findddd.lower():
                s.display()
                found=True
                break
        if not found:
            print("Student not found")
    elif choice==5:
        found=False
        getout=input("Enter name to remove:\n").strip()
        for s in students:
            if s.name.lower()==getout.lower():
                students.remove(s)
                print("Student succesfully removed\n")
                Student.save_students(students)
                found=True
                break
        if not found:
            print("Student not found")
    else:
        print("byee")
        break

