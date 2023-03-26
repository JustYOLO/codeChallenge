from sys import stdin; input = stdin.readline

s = input().rstrip()
for i in range(len(s)//2):
    if s[i] != s[-1*(i+1)]:
        print(0)
        exit()
print(1)