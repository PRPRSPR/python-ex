print("Hello Python")

num = 10
print(type(num))
# js처럼 자동으로 type판단 >> int

num = True
print(type(num))
# true,false 는 앞자리 대문자 True,False >> bool

print(num)
print(type(num), num)
# 알아서 줄바꿈. 줄바꿈 없이 출력하려면 ','로 구분

print(10/4) # =2.5
print(10//4) # =2
# return type을 따로 지정해주지 않기 때문에 나눠져있음

# a<10 and b>30 , a<10 or b>30 , not a>10
# a<10 && b>30 , a<10 || b>30 , !a>10

head = 'python'
tail = ' is fun'
print(head+tail)
# 문자열 더하기 >>> 'python is fun'

word = 'happy '
print(word*3)
# 문자열 곱하기 >>> 'happy happy happy '

temp = input('입력 : ')
print(temp)
# 입력한 값이 temp에 담김

a = input('첫번째 숫자 : ')
b = input('두번째 숫자 : ')
print(a+b)
# a = 10, b = 20 >> 1020 출력  >>>  디폴트가 문자열이기 때문

a = int(input('첫번째 숫자 : '))
b = int(input('두번째 숫자 : '))
print(a+b)
# int 정수형으로 변환 >>> 30 출력 // 실수형으로 변환 >> float

# ','를 이용해 출력, '%s','%d'등을 이용해 출력
# format() 이용해 출력, f-string을 이용해 출력

# f-string 사용
name = input('이름 : ')
age = input('나이 : ')
print(f'{name}의 나이는 {age}입니다.')

txt = 'asdfgh'
# [start : end : step] 0부터 시작. 
print(txt[4:5])
# 5번째부터 6번째 >> gh
print(txt[:3])
# start가 생략. 0부터 3까지. >>> asd
print(txt[::2])
# start, end가 생략. 처음부터 끝까지. step 2 >>> 2개씩 건너서. 0,2,4 >>> adg

list = [10, 20, 30, 40]
print(list)
# [10, 20, 30, 40]
print(list[2])
# 30
print(list[1:3])
# [20, 30] >> 1번 : 20 / 끝-1 이기 때문에 30

list[0] = 50
# [50, 20, 30, 40]
list[1:3] = [60, 70]
# [50, 60, 70, 40]

