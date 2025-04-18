# 각 과목의 점수를 보내서 총점, 평균을 리턴
# def score(kor, eng, math) :
#     sum = kor + eng + math
#     avg = sum / 3
#     return sum, avg

# total, average = score(90, 93, 96)
# print(total)
# print(average)
# print(f"{average:.2f}")
# :.2f >> 소수점 2자리까지


# 값을 tuple로 받아 가변처리

def score(*sub_scores) :
    score_sum = sum(sub_scores)
    score_avg = score_sum / len(sub_scores)
    return score_sum, score_avg

total, average = score(90, 93, 96)
print(total)
print(average)
print(f"{average:.2f}")