'''
소수 찾기

문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''
# calcuate all (2 ~ n-1)
'''
import sys
sys.stdin.readline()
nlist = list(map(int, sys.stdin.readline().split()))
result = nlist[:]
for n in nlist:
    if n == 1: 
        result.remove(n)
        continue
    for i in range(2, n):
        if n%i == 0:
            result.remove(n)
            break
print(len(result))
'''
# calcuate smaller than sqrt
import sys
from math import sqrt, ceil
def isPrime(n):
    if n == 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True
sys.stdin.readline()
nlist = list(map(int, sys.stdin.readline().split()))
result = nlist[:]
for n in nlist: 
    if not isPrime(n): result.remove(n)
print(len(result))