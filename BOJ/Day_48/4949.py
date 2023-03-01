from sys import stdin; input = stdin.readline

while True:
    flag = False
    string = input().rstrip()
    if len(string) == 1 and string[0] == ".":
        break
    arr = list()
    for char in string:
        if char == "[": arr.append(0)
        elif char == "]":
            if len(arr) == 0:
                flag = True
                print("no")
                break
            else:
                if arr.pop() != 0:
                    flag = True
                    print("no")
                    break
        elif char == "(": arr.append(1)
        elif char == ")":
            if len(arr) == 0:
                flag = True
                print("no")
                break
            else:
                if arr.pop() != 1:
                    flag = True
                    print("no")
                    break
    if not flag:
        if len(arr) == 0: print("yes")
        else: print("no")