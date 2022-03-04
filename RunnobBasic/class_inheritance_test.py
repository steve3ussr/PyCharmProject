class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__grade = None

    def set_grade(self, i):
        self.__grade = i

    def print_age(self):
        print(f"{self.name}的年龄是{self.age}")

    def print_grade_level(self):
        if self.__grade >= 90:
            print(f"{self.name}的成绩是优")
        elif self.__grade >= 60:
            print(f"{self.name}的成绩是还行")
        else:
            print(f"{self.name}的成绩是寄")


class Teacher(Student):
   # 继承的时候公有属性自然不用写，私有属性通过函数来添加，就没必要写__init__
    def set_wage(self, i):
        self.__wage = i

    def print_wage(self):
        print(f"{self.name}的工资是{self.__wage}")


# initialization
list_student_name  = ['Alice Whitman', 'Colin McRae']
list_student_age   = [16, 25]
list_student_grade = [59, 100]
list_teacher_name  = ['Yigang Wang', 'Zhigang Yang']
list_teacher_age   = [57, 61]
list_teacher_wage  = [10000, 20000]

alice = Student(list_student_name[0], list_student_age[0])
colin = Student(list_student_name[1], list_student_age[1])
xiaogang = Teacher(list_teacher_name[0], list_teacher_age[0])
dagang = Teacher(list_teacher_name[1], list_teacher_age[1])
list_student_mem   = [alice, colin]
list_teacher_mem   = [xiaogang, dagang]

for mem, grade in zip(list_student_mem, list_student_grade):
    mem.set_grade(grade)

for mem, wage in zip(list_teacher_mem, list_teacher_wage):
    mem.set_wage(wage)

# test
if __name__ == '__main__':
    for mem in list_student_mem:
        mem.print_age()
        mem.print_grade_level()

    for mem in list_teacher_mem:
        mem.print_age()
        mem.print_wage()
