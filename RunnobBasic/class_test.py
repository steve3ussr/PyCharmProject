class Student(object):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_age(self):
        print(f"{self.name}的年龄是：{self.age}")

    def print_grade_level(self):
        if self.grade >= 90:
            print(f"{self.name}的成绩是：牛B")
        elif self.grade >= 80:
            print(f"{self.name}的成绩是：良")
        elif self.grade >= 70:
            print(f"{self.name}的成绩是：中")
        elif self.grade >= 60:
            print(f"{self.name}的成绩是：及格")
        else:
            print(f"{self.name}的成绩是：寄")


# create inst
alice = Student("Alice Whitman", "12", 24)
colin = Student("Colin McRae", "25", 100)


list_student = [alice, colin]
for mem in list_student:
    mem.print_grade_level()
