'''
최댓값

문제
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
'''
# Using max:
'''
import sys
nlist = []
for i in range(9):
    nlist.append(int(sys.stdin.readline()))
biggest = max(nlist)
position = 0
for i in range(len(nlist)):
    if biggest == nlist[i]: position = i+1
print(biggest)
print(position)
''' # Not using max:
import sys
biggest = 0
position = 0
for i in range(9):
    n = int(sys.stdin.readline())
    if biggest < n: 
        biggest = n
        position = i + 1
print(biggest)
print(position)