import time
from sys import stdin; input = stdin.readline

'''start = time.time()
while True:
    if time.time() - start > 0.1:
        break
    else:
        print(input().rstrip())'''
# Using EOF error
while True:
    try:
        print(input().rstrip())
    except:
        break