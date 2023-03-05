from sys import stdin; input = stdin.readline
from collections import deque
arr = deque([])
for _ in range(int(input())):
    line = input().rstrip()
    if "push" in line:
        tmp, n = line.split(); n = int(n)
        arr.append(n)
    elif "pop" in line:
        if len(arr) == 0: print(-1)
        else: print(arr.popleft())
    elif "size" in line: print(len(arr))
    elif "empty" in line:
        if len(arr) != 0: print(0)
        else: print(1)
    elif "front" in line:
        if len(arr) == 0: print(-1)
        else: print(arr[0])
    elif "back" in line:
        if len(arr) == 0: print(-1)
        else: print(arr[-1])