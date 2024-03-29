'''
곱셈

문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
'''
from sys import stdin; input = stdin.readline

def func(a, b, c):
    if b == 1:
        return a % c
    else:
        x = func(a, b//2, c)
        if b % 2 == 0: return (x**2) % c
        else: return ((x**2) * a) % c

a, b, c = map(int, input().split())
print(func(a,b,c))