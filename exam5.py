# def add(x, y) :
#     print(x+y)

def add(x, y=10) :
    print(x+y)

add(1,2)
# # 3

add(y=3, x=1)
# # 4

add(3)
# # y=10 / 13

# list = [1,2,3,4,5]
# print(sum(list))

def add(*num) :
    print(num)
    return sum(num)

print(add(1,2))
print(add(1,2,3,4,5,6,7,8,9,10))
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) // 55 출력

# def info(**user) :
#     print(user)

def info(**user) :
    for key, value in user.items() :
        print(f"{key}:{value}")

info(name="홍길동", age=30, addr="인천")
# {'name': '홍길동', 'age': 30, 'addr': '인천'} key:value(딕셔너리)형식 

def test() :
    print(10)

test()
# 10 출력

num = test()
print(num)
# num >> None 출력 // return 값 없음

