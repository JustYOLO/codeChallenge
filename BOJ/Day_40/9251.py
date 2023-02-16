'''
LCS

문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''
# 1st try: time exceeded (I printed the longest subsequence itself. The problem wants me to print the length)
'''from sys import stdin

s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()
arr = list()
pool = set()
for c2 in s2:
    arr.append([i for i, c in enumerate(s1) if c == c2])
for num in arr[0]:
    pool.add((num, s2[0]))
for i in range(1, len(s2)):
    buffer = list()
    for num in arr[i]:
        isAdd = False
        big = 0
        for case in pool:
            if case[0] < num and big < len(case[1]):
                isAdd = True
                big = len(case[1])
                tmp = (num, case[1] + s2[i])
        if isAdd:
            buffer.append(tmp)
        else:
            buffer.append((num, s2[i]))
    pool.update(buffer)
ans = ''
for case in pool:
    if len(case[1]) > len(ans):
        ans = case[1]
print(ans)'''

# 2nd try:
from sys import stdin

s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()
arr = [0 for i in range(len(s2))]
for i in range(len(s1)):
    big = 0
    for j in range(len(s2)):
        if big < arr[j]:
            big = arr[j]
        elif s1[i] == s2[j]:
            arr[j] = big + 1
print(max(arr))