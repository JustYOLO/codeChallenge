from sys import stdin; input = stdin.readline

N = int(input())
for _ in range(N):
    flag = False
    string = input().rstrip()
    arr = list()
    if string[0] == ")":
        print("NO")
        continue
    for char in string:
        if char == "(": arr.append(0)
        else:
            if len(arr) == 0:
                print("NO")
                flag = True
                break
            else: arr.pop()
    if not flag:
        if len(arr) == 0: print("YES")
        else: print("NO")