from sys import stdin; input = stdin.readline
from collections import deque

for _ in range(int(input())):
    result = 0
    N, M = map(int, input().split())
    d = deque(list(map(int, input().split())))
    while True:
        if N == 1: 
            print(1)
            break
        tmp = d.popleft()
        if len(d) == 0:
            print(result+1)
            break
        elif tmp >= max(d): 
            result += 1
            M -= 1
            if M < 0:
                print(result)
                break
        else:
            d.append(tmp)
            if M == 0: M = len(d) - 1
            else: M -= 1