'''
팩토리얼 0의 개수

문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.
'''
from sys import stdin
n = int(stdin.readline())
twos = 0
fives = 0
for i in range(1, n+1):
    while True:
            if i%2 == 0: 
                while i%2 == 0:
                    twos += 1
                    i //= 2
            elif i%5 == 0:
                while i%5 == 0:
                    fives += 1
                    i //= 5
            else:
                break
print(min(twos, fives))