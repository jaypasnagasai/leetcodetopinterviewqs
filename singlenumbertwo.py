# 137. Single Number II

class Solution:
    def singleNumber(self, nums):
        return next(num for num, cnt in Counter(nums).items() if cnt == 1)
