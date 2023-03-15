'''
이항 계수 3

문제
자연수 
\(N\)과 정수 
\(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 
\(N\)과 
\(K\)가 주어진다. (1 ≤ 
\(N\) ≤ 4,000,000, 0 ≤ 
\(K\) ≤ 
\(N\))

출력
 
\(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 출력한다.
'''
# use Feramt's little Theorem and modulo arithmetic
from sys import stdin; input = stdin.readline

PRIME = 1_000_000_007
N, K = map(int, input().split())

def fac_mod(N):
    result = 1
    for i in range(2, N+1): result = (result * i) % PRIME
    return result
def pow_mod(N, K):
    if K == 0: return 1
    elif K == 1: return N
    x = pow_mod(N, K//2)
    if K % 2 == 0: return (x**2) % PRIME
    else: return ((x**2) * N) % PRIME
print(fac_mod(N) * pow_mod((fac_mod(N-K) * fac_mod(K) % PRIME), PRIME - 2) % PRIME)