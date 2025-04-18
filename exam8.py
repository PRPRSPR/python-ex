# 1. 문자열 뒤집기 함수
# def reverse_string(s):
# 	pass

# reverse_string 함수 완성시키기

def reverse_string(s):
    return s[::-1]

print(reverse_string("asdfgh jkl;'"))



# 2. 중복 없는 로또 번호 생성기
# 1부터 45까지 숫자 중 중복 없이 6개를 랜덤으로 골라 리스트로 반환하는 함수
# sample() 함수 사용 금지

# def lotto():
# 	list = []
# 	return list

# lotto 함수 완성시키기

import random

def lotto():
	list = []
	while len(list) < 6:
		ran = random.randint(1, 45)
		if ran not in list :
			list.append(ran)
	return list
	
print(lotto())



# 3. 단어별 첫 글자 대문자로 바꾸기 (타이틀 케이스)
# "this is a title" → "This Is A Title"
# str.title() 함수 사용 금지

# def to_title_case(text):
# 	pass

# to_title_case 함수 완성시키기

def to_title_case(text):
	words = text.split()
	result = ""
	for word in words :
		result += word[0].upper() + word[1:].lower()+ " "
	return result

print(to_title_case("have a good day"))
    

def to_title_case2(text):
	words = text.split()
	resultList = []
	for word in words :
		resultList.append(word[0].upper() + word[1:].lower())
	return ' '.join(resultList)

print(to_title_case2("have a good day"))



# 4. 리스트 압축 함수 만들기
# 연속된 동일 요소들을 하나의 요소로 압축
# 예: [1, 1, 2, 2, 2, 3, 1, 1] → [1, 2, 3, 1]

# def compress_list(list):
# 	pass
	
# compress_list 함수 완성시키기

def compress_list(list):
	result = [list[0]]
	for i in range(1, len(list)):
		if list[i] != list [i-1]:
			result.append(list[i])
	return result

print(compress_list([1,1,2,2,3,1,1]))


# 5. 자리수 분리 및 합계 구하기
# 정수 하나를 입력받아, 각 자리의 숫자를 분리해서 리스트로 반환하고,
# 그 자리수들의 합도 같이 반환하는 함수

# func(1234) → ([1, 2, 3, 4], 10)
# func(908) → ([9, 0, 8], 17)

# def split_sum(num) : 
# 	pass

def split_sum(number) : 
	digits = [int(num) for num in str(number)]
	total = sum(digits)
	return digits, total

print(split_sum(1352))