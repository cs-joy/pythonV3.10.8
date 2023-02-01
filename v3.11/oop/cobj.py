class Student:
    all = []

    def __init__(self, name: str, id: int, dept: str):
        assert id >= 1, f"less than 1"

        self.name = name
        self.id = id
        self.dept = dept

        Student.all.append(self)

    def __repr__(self):
        return f"Student('{self.name}', '{self.id}', '{self.dept}')"


student1 = Student("Md. Zahangir Alam", 202010019, "CSE")
student2 = Student("Md. Nayem Hossain", 202011034, "CSE")
student3 = Student("Md. Rupok Ahmed", 202021909, "CSE")
student4 = Student("Md. Rashid", 20210219, "CS")
student5 = Student("Md. Maruf Alam", 2020109, "CSE")
student6 = Student("Md. Nasim Alam", 2023019, "CSE")
student7 = Student("Md. Kawsar Ahmed", 20181019, "BBA")

print(Student.all)
