'''
스타트와 링크

문제
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5	 
예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

입력
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.
'''
# 1st try: passed (pypy3: 872ms)
'''from sys import stdin
from itertools import combinations

n = int(stdin.readline())
arr = list(list(int(j) for j in stdin.readline().split()) for i in range(n))
players = set(i for i in range(n))
min = 1e10
for team1 in combinations(players, n//2):
    team1 = set(team1)
    team2 = players - team1
    t1_pow = 0
    t2_pow = 0
    for i in team1:
        for j in team1:
            if i == j: continue
            t1_pow += arr[i][j]
    for i in team2:
        for j in team2:
            if i == j: continue
            t2_pow += arr[i][j]
    if min > abs(t1_pow - t2_pow):
        min = abs(t1_pow - t2_pow)
print(min)'''
# another method?
# Not that fast (pypy3: 1384ms)
from sys import stdin
from itertools import combinations

n = int(stdin.readline())
table = list(list(int(j) for j in stdin.readline().split()) for i in range(n))
players = set(i for i in range(n))
min = 1e10
for team1 in combinations(players, n//2):
    arr = [line[:] for line in table]
    team1 = set(team1)
    t1_pow = 0
    for i in team1:
        for j in range(n):
            if j in team1:
                t1_pow += arr[i][j]
                t1_pow += arr[j][i]
            arr[i][j] = 0
            arr[j][i] = 0
    t2_pow = 0
    for line in arr:
        t2_pow += sum(line)
    if min > abs(t1_pow - t2_pow):
        min = abs(t1_pow - t2_pow)
print(min)