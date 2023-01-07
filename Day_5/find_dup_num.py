'''
annotation: https://www.youtube.com/watch?v=pKO9UjSeLew
https://fierycoding.tistory.com/45
https://leetcode.com/problems/find-the-duplicate-number/

'''
def findDuplicate(num):
    for i in range(len(num) - 1):
        if(num[i] == num[i+1]): 
            print(num[i])
            break