import random

print(random.randint(1,10))
# 1~10 사이 랜덤 값 출력

# 정답에 0을 입력하기 전까지 랜덤 구구단 문제 출력
# 정답 맞추면 '정답' 아니면 '오답'
# 0 입력 시 '종료되었습니다.'

while True :
    x = random.randint(2,9)
    y = random.randint(1,9)
    print(f"{x}x{y} = ? ")
    user = int(input("정답 : "))
    if (x*y) == user :
        print("정답")
    elif user == 0 :
        print("종료되었습니다.")
        break
    else :
        print("오답")



# up and down 랜덤숫자 (1~100)
# 몇번만에 맞췄는지

ran = random.randint(1,100)
count = 0
while True :
    user = int(input("Up and Down : "))
    count+=1
    if user < ran :
        print("Up")
    elif user > ran :
        print("Down")
    elif user == ran :
        print(f"정답! {count}번만에 성공")
        break
    else : 
        print("잘못된 입력")

