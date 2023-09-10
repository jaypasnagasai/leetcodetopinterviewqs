# 128. Longest Consecutive Sequence

class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        count = 0
        temp = 1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        for i in range(len(nums) - 1):
            if nums[i] == (nums[i + 1] - 1):
                temp += 1
                count = max(count, temp)
            elif nums[i] == (nums[i + 1]):
                count = max(count, temp)
            else:
                temp = 1
                count = max(count, temp)
        return count
