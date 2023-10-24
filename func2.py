# func2.py
# 스코핑룰(LGB 규칙)

x = 1
def func1(a):
    return a+x

# 호출
print(func1(1))

def func2(a):
    x = 5
    return a+x

# 호출
print(func2(1))