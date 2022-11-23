def solution(strings, n):
    answer = []
    #strings를 각 문자열 길이로 정렬하기
    # strings.sort(key = lambda x: len(x))
    # answer = strings
    #strings를 정렬하기
    strings.sort() #["abce", "abcd", "cdx"] -> ["abcd", "abce", "cdx"]
    #n번째 문자로 정렬하기
    strings.sort(key = lambda x: x[n])
    #strings를 answer에 넣기
    answer = strings
    return answer

result = solution(["sun", "bed", "car"], 1)
print(result)   #["car", "bed", "sun"]
result = solution(["abce", "abcd", "cdx"], 2)
print(result)   #["abcd", "abce", "cdx"]