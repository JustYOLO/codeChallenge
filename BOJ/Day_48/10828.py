from sys import stdin; input = stdin.readline

N = int(input())
arr = list()
for _ in range(N):
    string = input().rstrip()
    if "push" in string:
        tmp, num = string.split()
        arr.append(int(num))
    elif string == "pop":
        if len(arr) == 0: print(-1)
        else: print(arr.pop())
    elif string == "size": print(len(arr))
    elif string == "empty":
        if len(arr) == 0: print(1)
        else: print(0)
    elif string == "top":
        if len(arr) == 0: print(-1)
        else: print(arr[-1])