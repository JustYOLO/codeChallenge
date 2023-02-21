'''
체스판 다시 칠하기 2

문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 K×K 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 K×K 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 K×K 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N, M, K가 주어진다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 잘라낸 K×K 보드를 체스판으로 만들기 위해 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

제한
1 ≤ N, M ≤ 2000
1 ≤ K ≤ min(N, M)
'''
# 1st try: time exceeded
# Need to use 2d-sum (see 11660.py)
'''from sys import stdin
N, M, K = map(int, stdin.readline().split())

def count_board(arr, isWhite):
    result = list()
    wb = ['B', 'W']
    if isWhite: wb = wb[::-1]

    for i in range(N):
        line = [0]
        for j in range(M):
            if i%2==0 and j%2==0:
                if arr[i][j] == wb[0]: line.append(line[-1])
                else: line.append(line[-1] + 1)
            elif i%2==0 and j%2==1:
                if arr[i][j] == wb[1]: line.append(line[-1])
                else: line.append(line[-1] + 1)
            elif i%2==1 and j%2==0:
                if arr[i][j] == wb[1]: line.append(line[-1])
                else: line.append(line[-1] + 1)
            elif i%2==1 and j%2==1:
                if arr[i][j] == wb[0]: line.append(line[-1])
                else: line.append(line[-1] + 1)
        result.append(line)
    return result

board = [stdin.readline().rstrip() for i in range(N)]

wboard = count_board(board, True)
bboard = count_board(board, False)
min = 1e10

for i in range(N-K+1):
    for j in range(1, M-K+2):
        wsum = 0
        bsum = 0
        for line in range(K):
            wsum += wboard[i+line][j+K-1] - wboard[i+line][j-1]
            bsum += bboard[i+line][j+K-1] - bboard[i+line][j-1]
        if min > wsum: min = wsum
        if min > bsum: min = bsum
print(min)'''
# 2nd try
from sys import stdin, maxsize
def count_board(color):
    arr = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            if (i+j) % 2 == 0: num = board[i][j] != color
            else: num = board[i][j] == color
            arr[i+1][j+1] = arr[i][j+1] + arr[i+1][j] - arr[i][j] + num
    count = maxsize
    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
            result = min(count, arr[i + K - 1][j + K - 1] - arr[i + K - 1][j - 1] - arr[i - 1][j + K - 1] + arr[i - 1][j - 1])
    return result

N, M, K = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(N)]
print(min(count_board('W'), count_board('B')))