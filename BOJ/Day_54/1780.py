from sys import stdin; input = stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = {-1:0, 0:0, 1:0}

def isPaper(x, y, N):
    colour = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if colour != paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        isPaper(x+(N//3)*a, y+(N//3)*b, N//3)
                return
    if colour == -1:
        result[-1] += 1
    elif colour == 0:
        result[0] += 1
    else:
        result[1] += 1
isPaper(0,0,N)
print(result[-1])
print(result[0])
print(result[1])