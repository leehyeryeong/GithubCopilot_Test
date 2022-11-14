def solution(array):
    answer = 0
    array.sort()
    if len(array)%2 == 0:
        answer = (array[len(array)//2]+array[len(array)//2-1])/2
    else:
        answer = array[len(array)//2]
    return answer

result = solution([1, 2, 7, 10, 11])
print(result)   #7
result = solution([9, -1, 0])
print(result)   #0