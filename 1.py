class Course:
  def _str_(self, course_name,course_id,course_credits):
    self.course_name = course_name
    self.course_id = course_id
    self.course_credits = course_credits
    def _str_(self):
       return f"Name: {self.course_name}\nID = {self.stu_id}\nCourse = {self.course_info}"
    def get(self):
       return f"Name: {self.course_name}\nID = {self.stu_id}\nCourse = {self.course_info}"
class Student:
   def _init_(self,stu_name, stu_id):
     self.stu_name = stu_name
     self.stu_id = stu_id
     self.course
     
def get(self):
   return f"Name: {self.stu_name}\nID = {self.stu_id}\nCourse = {self.getInfo()}"
def addCourse(self,object):
     self.course_info = object
c1 = Course(course_name = "套裝軟體應用",course_id = "G0D17M01",course_credits = "3")
s1 = Student(stu_name = "陳妍蓉",stu_id = "4b1k0026")
s1.addCourse(course_info = c1)
print(s1)






class Person:
    def _init_(self,name, age ):
     self.name = name
     self.age = age

    def _str_(self):
     return f"Name: {self.name}\nAge = {self.age}"
p1 = Person ("John",36)
print(p1)
p2 = Person("Sue",22)
print(p2._dict_)