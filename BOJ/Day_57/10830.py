from sys import stdin; input = stdin.readline

def power_of_matrix(m1, m2):
    result = list()
    for i in range(len(m1)):
        line = list()
        for j in range(len(m2)):
            sum = 0
            for a in range(len(m2)):
                sum += (m1[i][a] * m2[a][j]) % 1000
            line.append(sum%1000)
        result.append(line)
    return result

def func(matrix, b):
    if b == 1:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] %= 1000
        return matrix
    elif b == 2:
        return power_of_matrix(matrix, matrix)
    else:
        if b%2 == 0:
            m1 = func(matrix, b//2)
            return power_of_matrix(m1, m1)
        else:
            m1 = func(matrix, b//2)
            m2 = power_of_matrix(m1, m1)
            return power_of_matrix(m2, matrix)

N, B = map(int, input().split())
iMtx = list()
for _ in range(N):
    iMtx.append(list(map(int, input().split())))
for line in func(iMtx, B):
    for num in line:
        print(num, end=" ")
    print()