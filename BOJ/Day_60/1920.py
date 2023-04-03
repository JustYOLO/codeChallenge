# 1st attempt: not using binary search => time exceeded
'''
from sys import stdin; input = stdin.readline
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
for num in arr2:
    if num in arr1: print(1)
    else: print(0)
'''
# 2nd attempt: using binary search
from sys import stdin; input = stdin.readline

def binary_search(arr, num):
    low = 0; high = len(arr)-1;
    while low + 1 < high:
        mid = (low + high)//2
        if arr1[mid] == num: 
            return 1
        elif arr1[mid] < num:
            low = mid
        elif arr1[mid] > num:
            high = mid
    if arr[low] == num or arr[high] == num: return 1
    return 0

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()
for num in arr2:
    print(binary_search(arr1, num))