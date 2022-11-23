#OX퀴즈

def solution(quiz):
    answer = []
    #quiz를 하나씩 꺼내기
    for i in quiz: #i "3 - 4 = -3"
        #i를 공백으로 나누기
        i = i.split(" ") #i ["3", "-", "4", "=", "-3"]
        #i의 0번째를 num1
        num1 = int(i[0])
        #i의 1번째를 operator
        operator = i[1]
        #i의 2번째를 num2
        num2 = int(i[2])
        #i의 4번째를 result
        result = int(i[3])
        #num1과 num2를 operator로 계산하기
        if operator == "+":
            if num1+num2 == result:
                answer.append("O")
            else:
                answer.append("X")
        elif operator == "-":
            if num1-num2 == result:
                answer.append("O")
            else:
                answer.append("X")
    return answer

result = solution("3 - 4 = -3", "5 + 6 = 11")
print(result)   #["X", "O"]