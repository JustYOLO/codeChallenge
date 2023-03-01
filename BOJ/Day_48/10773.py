from sys import stdin; input = stdin.readline

arr = list()
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)
print(sum(arr))