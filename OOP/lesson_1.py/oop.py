

class Student:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100
        
    def get_grade(self):
        return self.grade
        

class Course:
    def __init__(self, name: str, max_students: int):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False
        
    def get_average_student(self):
        value = 0
        for students in self.students:
            value += students.get_grade()
            
        return value / len(self.students)
    
        




st1 = Student("Anna", 12, 86)
st2 = Student("Ivan", 11, 80)
st3 = Student("Dmytro", 35, 60)

course = Course("Science", 2)
course.add_student(st1)
course.add_student(st2)

print(course.students[1].age)

print(course.get_average_student())



















# class Student: 
#     def __init__(self, name: str, age: int, grade: int) -> None:
#         self.name = name
#         self.age = age
#         self.grade = grade # 0 - 100
        
#     def get_grade(self):
#         return self.grade
    
# class Course:  
#     def __init__(self, name: str, max_students: int) -> None:
#         self.name = name
#         self.max_students = max_students
#         self.students = []
        
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         else:
#             return False
        
#     def get_average_grade(self):
#         # pass
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
            
#         return value / len(self.students)    

# s1 = Student("Anna", 13, 75)
# s2 = Student("Kiril", 12, 80)
# s3 = Student("Ivan", 12, 78)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# # course.add_student(s3)

# print(course.students[2].name)
# print(course.get_average_grade())




