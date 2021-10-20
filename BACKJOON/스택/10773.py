# 제로 

'''
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)

이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 

정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.

정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

'''

# 입력된 수로 누적합 구하기
# 0이 될때마다 pop 

from sys import stdin
n = int(stdin.readline())


arr = []
for _ in range(n):
    arr.append(int(stdin.readline()))


answer = []

for i in arr:
    
    if i == 0:
        del answer[-1]
    else:
        answer.append(i)


print(sum(answer))