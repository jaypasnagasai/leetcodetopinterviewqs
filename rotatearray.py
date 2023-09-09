# 189. Rotate Array

class Solution:
    def rotate(self, nums, k):
        if k >= len(nums):
            k = k%len(nums)
        if len(nums)==1 or k == 0:
            return nums
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        return nums
