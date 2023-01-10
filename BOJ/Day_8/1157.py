'''
단어 공부

문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''
# not using set()
'''
import sys
s = sys.stdin.readline().rstrip()
s = s.upper()
dic = {}
for c in s:
    if c not in dic: dic[c] = 1
    else: dic[c] = dic[c] + 1
count = 0
max_c = max(dic, key=dic.get)
for c in dic.keys():
    if max_c == c: continue
    elif dic[max_c] == dic[c]:
        print("?")
        exit()
print(max_c)
'''
# using set()
import sys
s = sys.stdin.readline().rstrip()
s = s.upper()
word = list(set(s))
cnt = []
for c in word:
    n = s.count(c)
    cnt.append(n)
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word[cnt.index(max(cnt))])