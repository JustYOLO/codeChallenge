'''
N-Queen

문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''
from sys import stdin
count = 0
def search(i, col):
    global count
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            count += 1
        else:
            for j in range(1, n+1):
                col[i+1] = j
                search(i+1, col)

def promising(i, col):
    k = 1
    flag = True
    while k < i:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
            break
        k += 1
    return flag
n = int(stdin.readline())
col = [0] * (n+1)
search(0, col)
print(count)