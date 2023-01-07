'''
annotation: https://www.youtube.com/watch?v=pKO9UjSeLew
https://fierycoding.tistory.com/45
https://leetcode.com/problems/find-the-duplicate-number/

'''
''' Not using Floyd's Tortoise and Hare
from typing import List

class Solution:
    def __init__(self) -> None:
        pass
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if(nums[i] == nums[i+1]):
                return nums[i]
                break

s = Solution()
s.findDuplicate(nums=[1, 2, 3, 4, 5, 1])
''' 
# Using Floyd's Tortoise and Hare
from typing import List

class Solution:
    def __init__(self) -> None:
        pass
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]
        while(True):
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if(tortoise == hare):
                tortoise = nums[0]
                break
        while(tortoise != hare):
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare
s = Solution()
print(s.findDuplicate(nums=[1, 4, 3, 5, 6, 1, 2]))
