from sys import stdin; input = stdin.readline
arr = list()
for _ in range(5):
    arr.append(input().rstrip())
while True:
    for i in range(5):
        try: 
            print(arr[i][0], end='')
            arr[i] = arr[i][1:]
        except:
            continue
    flag = True
    for i in range(5):
        if len(arr[i]) != 0:
            flag = False
    if flag: break