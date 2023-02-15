'''
가장 긴 바이토닉 부분 수열

문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.
'''
from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp1 = list()
dp2 = list()

dp1.append(1)
for i in range(1, N):
    big = 0
    for j in range(len(dp1)):
        if arr[j] < arr[i] and big < dp1[j]:
            big = dp1[j]
    dp1.append(big+1)
arr = arr[::-1]
dp2.append(1)
for i in range(1, N):
    big = 0
    for j in range(len(dp2)):
        if arr[j] < arr[i] and big < dp2[j]:
            big = dp2[j]
    dp2.append(big+1)
dp2 = dp2[::-1]
for i in range(N):
    dp1[i] += dp2[i] - 1
print(max(dp1))