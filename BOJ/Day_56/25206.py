from sys import stdin; input = stdin.readline

dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sum_credit = 0
sum_grade = 0
for _ in range(20):
    tmp, credit, grade = map(str, input().split())
    if grade != 'P':
        sum_credit += float(credit)
        sum_grade += dic[grade] * float(credit)
print(sum_grade/sum_credit)