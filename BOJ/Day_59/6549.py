# 1st attempt: time exceed
'''from sys import stdin; input = stdin.readline
from sys import setrecursionlimit
setrecursionlimit(10**6)

def find(start, width, height, hFlag, wFlag):
    if start + width < len(histogram):
        wbig = 0; hbig = 0
        if hFlag:
            for i in range(width):
                if histogram[start+i] < height + 1:
                    hFlag = False
                    break
        if wFlag and histogram[start+width] < height:
            wFlag = False
        if wFlag: 
            wbig = find(start, width+1, height, hFlag, wFlag)
        if hFlag: 
            hbig = find(start, width, height+1, hFlag, wFlag)
        if wFlag or hFlag:
            return wbig if wbig>hbig else hbig
    return width*height


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0 and len(arr) == 1: exit()
    histogram = arr[1:]
    result = list()
    for i in range(len(histogram)):
        if histogram[i] == 0: result.append(0)
        else: result.append(find(i, 1, 1, True, True))
    print(max(result))'''
# 2nd attempt: using stack
from collections import deque
from sys import stdin; input = stdin.readline

while True:
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    if n == 0: break
    stack = deque()
    result = 0

    for i in range(n):
        while len(stack) != 0 and arr[stack[-1]] > arr[i]: 
            tmp = stack.pop()

            if len(stack) == 0: width = i
            else: width = i - stack[-1] - 1
            result = max(result, width * arr[tmp])
        stack.append(i)
    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0: width = n
        else: width = n - stack[-1] - 1
        result = max(result, width*arr[tmp])
    print(result)