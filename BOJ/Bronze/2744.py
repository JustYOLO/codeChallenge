string = input().rstrip()
for char in string:
    if char.isupper():
        print(char.lower(), end="")
    else:
        print(char.capitalize(), end="")