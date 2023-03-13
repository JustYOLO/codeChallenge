from sys import stdin; input = stdin.readline

N = int(input())
paper = [list(map(int, input().rstrip())) for _ in range(N)]

def isPaper(x, y, N):
    colour = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if colour != paper[i][j]:
                print("(", end="")
                isPaper(x, y, N//2)
                isPaper(x, y+N//2, N//2)
                isPaper(x+N//2, y, N//2)
                isPaper(x+N//2, y+N//2, N//2)
                print(")", end="")
                return
    if colour == 0:
        print(0, end="")
    else:
        print(1, end="")
isPaper(0,0,N)