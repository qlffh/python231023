# 부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    def working(self):
        print("현재 작업중")
    def sleeping(self):
        print("현재 수면중")

# 자식 클래스
class Student(Person):
    # 초기화 메서드 덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        self.name = name
        self.phoneNumber = phoneNumber
        self.subject = subject
        self.studentID = studentID

# 인스턴스
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "201234")
print(p.__dict__)
print(s.__dict__)
p.printInfo()
s.printInfo()
s.working()
s.sleeping()

