'''
구간 합 구하기 4

문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

제한
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N
'''
# 1st try: time exceeded
'''from sys import stdin
N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
for _ in range(M):
    i, j = map(int, stdin.readline().split())
    print(sum(arr[i-1:j]))'''
# 2nd try: using prefix sum
from sys import stdin
N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
sum = [0]
for i in range(N):
    sum.append(arr[i] + sum[i])
for _ in range(M):
    i, j = map(int, stdin.readline().split())
    print(sum[j] - sum[i-1])