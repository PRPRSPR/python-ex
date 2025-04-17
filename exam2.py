t = (1, 2, 3, 4)
#     t[0] = 100
#     ~^^^
# TypeError: 'tuple' object does not support item assignment

tt = ([1,2,3], 2,3,4)
tt[0][1] = 100
print(tt)
#([1, 100, 3], 2, 3, 4)

ttt = (1)
print(type(ttt))
# ','로 구분하기 때문에 ttt는 int로 출력됨
# ttt = (1,)일 경우 tuple
# t = 1, 2, 3 일 경우에도 tuple
# t, a, b = 1, 2, 3 일 경우에는 int

menu = {"김밥":2000, "라면":3500, "어묵":1000}
print(menu.keys())
print(menu.values())
print(menu.items())
# dict_keys(['김밥', '라면', '어묵'])
# dict_values([2000, 3500, 1000])
# dict_items([('김밥', 2000), ('라면', 3500), ('어묵', 1000)])

name = {100 : "홍길동", 200 : "김철수", 300 : "박영희"}
del(name[300])
# print(del(name[300])) >> 오류
print(name)
# {100: '홍길동', 200: '김철수'}

print(name.pop(200))
# >> 김철수 출력
print(name)
# {100: '홍길동'}



# if문

num = int(input("숫자 입력 : "))
# 입력값이 5보다 크면 '5보다 큽니다'출력
# if(num > 5) { } <<java

if num > 5 :
    print("5보다 큽니다")
else : 
    print("5보다 작거나 같다")



# 숫자 하나 입력받아서 홀수, 짝수 구분


num = int(input("숫자 입력 : "))
if num % 2 == 0 :
    print("짝수")
else :
    print("홀수")


# 입장료 정가 2만원, 1~6세 미만 무료, 6~60세 미만 정가, 60세 이상 정가의 50%

price = 20000
age = int(input("나이 : "))
if 1 <= num < 6 :
    print("무료")
elif 6 <= age < 60 :
    print(f"가격은 {price}원")
elif 60 <= age :
    print(f"가격은 {price*0.5}원")
else :
    print("잘못된 입력")


# 리스트에 값이 포함되어있는지

fruit = ["apple", "orange", "banana"]
if "apple" in fruit : 
    print("사과 ㅇㅇ")
else : 
    print("사과 ㄴㄴ")


txt = "Hello Python"
if "Python" in txt :
    print("파이썬 있")

hong = {"name" : "홍길동", "age" : 30, "addr" : "인천"}
if "name" in hong :
    print("이름 ㅇ")

if "홍길동" in hong.values() :
    print("홍길동 ㅇ")

if "서울" not in hong.values() :
    print("서울 ㄴ")




# for문

for i in range(10) :
    print(i)

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

sum=0

for i in range(1, 11) :
    # range(1, 10+1)
    sum += i    
print(sum)


for i in range(2,10) :
    for j in range(1, 10) :
        print(f"{i}x{j}={i*j}")

for i in range(1,6) :
    print("*"*i)

list =  ["banana", "orange", "apple"]
for fruit in list :
    print(fruit)

list =  ["banana", "orange", "apple"]
for idx,fruit in enumerate(list) :
    print(f"{idx+1} : {fruit}")
# 1 : banana / 2 : orange / 3 : apple

text = "Hello Python"
for char in text :
    print(char, end=" ")
# H e l l o   P y t h o n

hong = {"name": "홍길동","age":30,"addr":"인천"}
for key, value in hong.items() :
    print(f"{key} : {value}")
# name : 홍길동 / age : 30 / addr : 인천

