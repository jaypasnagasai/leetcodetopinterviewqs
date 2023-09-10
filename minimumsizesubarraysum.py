# 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target, nums):
        res = len(nums) + 1
        l = s = 0
        for r, v in enumerate(nums):
            s += v
            while s >= target:
                s -= nums[l]
                res = min(res, r - l + 1)
                l += 1
        return 0 if res > len(nums) else res
