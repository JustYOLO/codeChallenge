'''
연속합

문제
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.
'''
# 1st try: memory exceeded: make arr pop unnecessary list
# 2nd try: time exceeded
'''
from sys import stdin
from itertools import pairwise

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split()))]
result = set(arr[0])
tmp = list()
for t in pairwise(arr[0]):
    tmp.append(sum(t))
arr.append(tmp[:])
result.update(tmp)
for i in range(2, n):
    tmp.clear()
    for j in range(n-i):
        tmp.append(arr[1][j]+arr[0][j+i])
    arr.pop()
    arr.append(tmp[:])
    result.update(tmp)
print(max(result))
'''
from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i] + arr[i-1])
print(max(arr))