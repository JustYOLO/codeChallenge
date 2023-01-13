'''
소인수분해

문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
'''
import sys
n = int(sys.stdin.readline())
if n == 1: exit()
nlist = []
for i in range(2, int(n**0.5) + 1):
    while n % i == 0:
        nlist.append(i)
        n = n//i
if n > 1: nlist.append(n)
for i in nlist:
    print(i)