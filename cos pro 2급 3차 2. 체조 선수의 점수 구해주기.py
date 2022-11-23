# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(scores):
    answer = 0
    #scores에서 가장 낮은 점수 제거하기
    scores.remove(min(scores))
    #scores에서 가장 높은 점수 제거하기
    scores.remove(max(scores))

    #scores의 평균 구하기
    answer = sum(scores)/len(scores)
    #answer에서 소수점 제거하기
    answer = int(answer)

    return answer

scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

print("solution 함수의 반환 값은", ret2, "입니다.")