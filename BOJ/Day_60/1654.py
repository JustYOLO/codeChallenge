from sys import stdin; input = stdin.readline

def getEach(arr, length):
    each = 0
    for num in arr:
        each += num//length
    return each

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
low = 0; high = sum(arr)//N
while low + 1 < high:
    mid = (low + high)//2 
    each = getEach(arr, mid)
    if each < N:
        high = mid
    else:
        low = mid
if getEach(arr, high) >= N: print(high)
else: print(low)