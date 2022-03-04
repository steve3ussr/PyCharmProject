class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print(f"{self.name}的年龄是{self.age}")

    def print_secret(self):
        pass


class Student(Human):
    def set_grade(self, i):
        self.__grade = i

    def print_grade_level(self):
        if self.__grade >= 90:
            print(f"{self.name}的成绩是优")
        elif self.__grade >= 60:
            print(f"{self.name}的成绩是还行")
        else:
            print(f"{self.name}的成绩是寄")

    def print_secret(self):
        print(f"{self.name}的秘密是：这次考试考了{self.__grade}")


class Teacher(Human):
    def set_wage(self, i):
        self.__wage = i

    def print_wage_level(self):
        if self.__wage >= 20000:
            print(f"{self.name}是大老板")
        elif self.__wage >= 10000:
            print(f"{self.name}是小老板")
        else:
            print(f"{self.name}是打工人")

    def print_secret(self):
        print(f"{self.name}的秘密是：这月工资拿了{self.__wage}")


# initialization
list_student_name = ['Alice Whitman', 'Colin McRae']
list_student_age = [16, 25]
list_student_grade = [59, 100]
list_teacher_name = ['Yigang Wang', 'Zhigang Yang']
list_teacher_age = [57, 61]
list_teacher_wage = [10000, 20000]

alice = Student(list_student_name[0], list_student_age[0])
colin = Student(list_student_name[1], list_student_age[1])
xiaogang = Teacher(list_teacher_name[0], list_teacher_age[0])
dagang = Teacher(list_teacher_name[1], list_teacher_age[1])
list_student_mem = [alice, colin]
list_teacher_mem = [xiaogang, dagang]

for mem, grade in zip(list_student_mem, list_student_grade):
    mem.set_grade(grade)

for mem, wage in zip(list_teacher_mem, list_teacher_wage):
    mem.set_wage(wage)

# test
if __name__ == '__main__':
    for mem in list_student_mem:
        mem.print_age()
        mem.print_grade_level()
        mem.print_secret()

    for mem in list_teacher_mem:
        mem.print_age()             # public base method
        mem.print_wage_level()      # methods in different subclasses
        mem.print_secret()          # methods in different subclasses
