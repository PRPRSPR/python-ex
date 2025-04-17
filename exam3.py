# 크기가 5인 리스트 생성 (모든 값 0으로 초기화)
# list = [0,0,0,0,0]
# list = [0] * 5
# print(list)

# # 리스트에 1~100까지 채워서 초기화
# list = [i for i in range(1, 100+1)]
# print(list)

# 숫자 5개 입력받아 list에 저장
list = []
for i in range(0,5) :
    num = int(input(f"{i+1}번째 숫자 입력 : "))
    list.append(num)
    # list.append(int(input(f"{i+1}번째 숫자 입력 : ")))
print(list)

list = [0]*5
for i in range(len(list)) : 
    list[i] = int(input(f"{i+1}번째 숫자 입력 : "))
print(list)
print(max(list))

hong = {"name": "홍길동","age":30,"addr":"인천"}
for key, value in hong.items() :
    print(f"{key} : {value}")

hong = {"name": "홍길동","age":30,"addr":"인천"}
for key in hong :
    print(f"{key} : {hong[key]}")