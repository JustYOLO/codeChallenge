'''
스도쿠 

문제
스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다. 이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.

나머지 빈 칸을 채우는 방식은 다음과 같다.

각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
위의 예의 경우, 첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로 첫째 줄 빈칸에는 1이 들어가야 한다.

또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이 이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.

이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.



게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

입력
아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다. 스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

출력
모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.

스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.

제한
12095번 문제에 있는 소스로 풀 수 있는 입력만 주어진다.
C++14: 80ms
Java: 292ms
PyPy3: 1172ms
'''
'''from sys import stdin

board = list(list(map(int, stdin.readline().split())) for i in range(9))
def print_board(board):
    for line in board:
        print(*line, sep=" ")

def search(r, c, board):
    if r == c and c == 8:
        if board[r][c] != 0:
            print_board(board)
            exit()
        else:
            for i in range(1, 10):
                board[8][8] == i
                if promising(8, 8, board, True):
                    print_board(board)
                    exit()
        return
    if board[r][c] == 0:
        if promising(r, c, board):
            if board[r][c] == 0:
                for i in range(1, 10):
                    board[r][c] = i
                    if c == 8:
                        search(r+1, 0, board)
                    else:
                        search(r, c+1, board)
        else: return
    else:
        if c == 8:
            search(r+1, 0, board)
        else:
            search(r, c+1, board)

def promising(r, c, board, end=False):
    rset = set()
    cset = set()
    for i in range(9):
        rset.add(board[r][i])
        cset.add(board[i][c])
    if (0 in rset or 0 in cset) and not end: pass
    elif end: return False
    elif len(rset) != 9 or len(cset) != 9: return False
    r //= 3; c //= 3
    rset.clear()
    for i in range(3):
        rset.add(board[r*3][c*3+i])
    for i in range(3):
        rset.add(board[r*3+1][c*3+i])
    for i in range(3):
        rset.add(board[r*3+2][c*3+i])
    if 0 in rset and not end: pass
    elif end: return False
    elif len(rset) != 9: return False
    return True
search(0, 0, board)'''
from sys import stdin

board = list(list(map(int, stdin.readline().split())) for i in range(9))
def print_board(board):
    for line in board:
        print(*line, sep=" ")

def search(r, c, board):
    if r == 8 and c == 8:
        if board[r][c] != 0:
            print_board(board)
            exit()
        else:
            for i in range(1, 10):
                board[8][8] = i
                if promising(8, 8, board, True):
                    print_board(board)
                    exit()
        return
    if board[r][c] == 0:
        for i in range(1, 10):
            board[r][c] = i
            if promising(r, c, board):
                if c == 8:
                    search(r+1, 0, board)
                else:
                    search(r, c+1, board)
            board[r][c] = 0
    else:
        if c == 8:
            search(r+1, 0, board)
        else:
            search(r, c+1, board)

def promising(r, c, board, end=False):
    rset = set()
    cset = set()
    for i in range(9):
        rset.add(board[r][i])
        cset.add(board[i][c])
    if (0 in rset or 0 in cset) and not end:
        pass
    elif end:
        return False
    elif len(rset) != 9 or len(cset) != 9:
        return False
    r //= 3; c //= 3
    rset.clear()
    for i in range(3):
        rset.add(board[r*3][c*3+i])
    for i in range(3):
        rset.add(board[r*3+1][c*3+i])
    for i in range(3):
        rset.add(board[r*3+2][c*3+i])
    if 0 in rset and not end:
        pass
    elif end:
        return False
    elif len(rset) != 9:
        return False
    return True

search(0, 0, board)
