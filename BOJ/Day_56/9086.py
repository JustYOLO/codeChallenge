from sys import stdin; input = stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    print(s[0]+s[-1])