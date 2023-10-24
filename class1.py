# 클래스 정의
class Person:
    # 초기화 메서드
    def __init__(self):
        # 멤버 변수 초기화
        self.name = "default name"
    # 멤버 메서드
    def print(self):
        print("My name is {0}".format(self.name))

# 인스턴스 생선
p1 = Person()
# 메서드 호출
p1.print()