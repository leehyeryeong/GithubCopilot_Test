print('test')
#hello world output
print('hello world')
#1~10까지 출력
for i in range(1,11):
    print(i)
#1~10까지 합
sum = 0
for i in range(1,11):
    sum += i
print(sum)
#1~10까지 홀수 출력
for i in range(1,11):
    if i%2 == 1:
        print(i)
#1~10까지 짝수 출력
for i in range(1,11):
    if i%2 == 0:
        print(i)
#1~10까지 홀수 합
sum = 0
for i in range(1,11):
    if i%2 == 1:
        sum += i
print(sum)
#1~10까지 짝수 합
sum = 0
for i in range(1,11):
    if i%2 == 0:
        sum += i
print(sum)
