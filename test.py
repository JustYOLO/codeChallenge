from math import sqrt

arr = list(map(float, input().split(", ")))
'''for str in tmp:
    score = float(f"{str[0]}.{str[1:]}")
    arr.append(score)'''
print(arr)
arr.sort()
diff_sum = 0
avg = 3.72
for score in arr:
    diff_sum += (score - avg)**2
print(diff_sum)
print(diff_sum/29)
print(sqrt(diff_sum/29))
s = sqrt(diff_sum/29)
s1 = 0
print(avg - s)
for score in arr:
    if score > avg - s and score < avg + s: 
        s1 +=1
        print(score)
print(s1)