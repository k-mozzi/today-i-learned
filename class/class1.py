result1 = 0
result2 = 0


def add1(num):  # 이전의 값을 메모리에 저장하는 함수
    global result1
    result1 += num
    return result1


def add2(num):
    global result2
    result2 += num
    return result2


print(add1(3))
print(add1(4))
print(add2(4))
print(add2(5))
