'''
분해합 다국어

문제
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.
'''
# brute force
'''import sys
def nsum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    n += sum
    return n
n = int(sys.stdin.readline())
for i in range(1, n):
    if nsum(i) == n:
        print(i)
        exit()
print(0)'''
# better way?
# href="https://developerhan.tistory.com/8"
import sys
def nsum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    n += sum
    return n
n = int(sys.stdin.readline())
if n - len(str(n))*9 < 0:
    for i in range(1, n):
        if nsum(i) == n:
            print(i)
            exit()
else:
    for i in range(n - len(str(n))*9, n):
        if nsum(i) == n:
            print(i)
            exit()
print(0)