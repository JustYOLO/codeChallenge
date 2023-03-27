from sys import stdin; input = stdin.readline

N, M = map(int, input().split())
m1 = list()
m2 = list()
for _ in range(N): m1.append(list(map(int, input().split())))
M, K = map(int, input().split())
for _ in range(M): m2.append(list(map(int, input().split())))
for i in range(N):
    for j in range(K):
        sum = 0
        for a in range(M):
            sum += m1[i][a] * m2[a][j]
        print(sum, end=" ")
    print()