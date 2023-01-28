'''
조합 0의 개수

문제

$n \choose m$의 끝자리 
$0$의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 
$n$, 
$m$ (
$0 \le m \le n \le 2,000,000,000$, 
$n \ne 0$)이 들어온다.

출력
첫째 줄에 
$n \choose m$의 끝자리 
$0$의 개수를 출력한다.
'''
from sys import stdin
def count_two(n):
    twos = 0
    while n != 0:
        n //= 2
        twos += n
    return twos
def count_five(n):
    fives = 0
    while n != 0:
        n //= 5
        fives += n
    return fives

n, m = map(int, stdin.readline().split())
print(min(count_five(n) - count_five(m) - count_five(n-m), count_two(n) - count_two(m) - count_two(n-m)))