from collections import Counter
nums = [2,2,2,2,1,1,1,1,4,4,5,5,6,6]
cnt = Counter(nums)
cnt.most_common(2)[1][1]