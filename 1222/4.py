#課程代碼、課程名稱、學分數、必選修、任課老師、上課時間
class Course:
    def __init__(self, course_id, course_name, course_hours, course_elective, course_teacher, course_time):
        self.course_id = course_id
        self.course_name = course_name
        self.course_hours = course_hours
        self.course_elective = course_elective
        self.course_teacher = course_teacher
        self.course_time = course_time

    def print_course_info(self):
        print(f"課程代碼: {self.course_id}")
        print(f"課程名稱: {self.course_name}")
        print(f"學分數: {self.course_hours}")
        print(f"必選修: {self.course_elective}")
        print(f"任課老師: {self.course_teacher}")
        print(f"上課時間: {self.course_time}")

    def get_course_time(self):
        return self.course_time
    
    def get_teacher(self):
        return self.course_teacher
c1 = Course(course_id="G0D17M01",course_name="套裝軟體應用",course_hours="3",course_elective="選修",course_teacher="李宗儒",course_time="8:00-11:00")

#列印課程資料
c1.print_course_info()

#查詢上課時間、查詢任課老師
print("上課時間:", c1.get_course_time())
print("任課老師:", c1.get_teacher())
