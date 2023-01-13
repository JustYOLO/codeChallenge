'''

'''
import sys
from math import sqrt, ceil
def isPrime(n):
    if n == 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
result = []
for i in range(m, n+1):
    if isPrime(i):
        result.append(i)
for i in result:
    print(i)