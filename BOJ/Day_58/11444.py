from sys import stdin; input = stdin.readline

DIVISION = 1_000_000_007

def multiple_of_matrix(m1, m2):
    result = list()
    for i in range(len(m1)):
        line = list()
        for j in range(len(m2[0])):
            sum = 0
            for a in range(len(m2)):
                sum += (m1[i][a] * m2[a][j]) % DIVISION
            line.append(sum%DIVISION)
        result.append(line)
    return result

def func(matrix, b):
    if b == 1:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] %= DIVISION
        return matrix
    elif b == 2:
        return multiple_of_matrix(matrix, matrix)
    else:
        if b%2 == 0:
            m1 = func(matrix, b//2)
            return multiple_of_matrix(m1, m1)
        else:
            m1 = func(matrix, b//2)
            m2 = multiple_of_matrix(m1, m1)
            return multiple_of_matrix(m2, matrix)

iMtx = [[1,1],[1,0]]
n = int(input())
maxtrix = multiple_of_matrix(func(iMtx, n), [[1], [0]])
print(maxtrix[1][0])