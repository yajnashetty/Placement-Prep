class Student:
    def __init__(self,name,roll_no,cgpa):
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa

    def details(self):
        print(f"name:{self.name}")
        print(f"roll no:{self.roll_no}")
        print(f"CGPA:{self.cgpa}")

    def update_cgpa(self,new_cgpa):
        self.cgpa = new_cgpa
        print("Cgpa updated succesfull")

    def is_passed(self):
        return self.cgpa>=6.0

stu_1 = Student("yajna shetty","4mt22ci061",7.45)
stu_1.details()
stu_1.update_cgpa(8.1)
print(f'passed? ',stu_1.is_passed())

