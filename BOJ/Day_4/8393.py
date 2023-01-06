'''
합 다국어

문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.
'''
'''
import sys

x = int(sys.stdin.readline())
sum = 0
for i in range(x):
    sum += i + 1
print(sum)
'''
import sys
x = int(sys.stdin.readline())
print((x*(x+1))//2)