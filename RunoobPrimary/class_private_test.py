class Student(object):
    def __init__(self, name, age):
        self.__grade = None
        self.name = name
        self.age = age

    def set_grade(self, num):
        self.__grade = num

    def print_age(self):
        print(f"{self.name}的年龄是：{self.age}")

    def print_grade_level(self):
        if self.__grade >= 90:
            print(f"{self.name}的成绩是：牛B")
        elif self.__grade >= 80:
            print(f"{self.name}的成绩是：良")
        elif self.__grade >= 70:
            print(f"{self.name}的成绩是：中")
        elif self.__grade >= 60:
            print(f"{self.name}的成绩是：及格")
        else:
            print(f"{self.name}的成绩是：寄")


# create inst
alice = Student("Alice Whitman", "12")
colin = Student("Colin McRae", "25")


list_student = [alice, colin]
list_score = [59, 100]

for mem, num_score in zip(list_student, list_score):
    mem.set_grade(num_score)
    mem.print_grade_level()

print(alice._Student__grade)
print(type(Student))
print(type(1))
print(type(int))
