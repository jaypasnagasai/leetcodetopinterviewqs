# 46. Permutations

class Solution:
    def permute(self, nums):
        def solve(nums, per, c):
            if c == len(nums):
                ans.append(list(per))
                return
            for i in range(len(nums)):
                if per[i] == 11:
                    per[i] = nums[c]
                    solve(nums, per, c + 1)
                    per[i] = 11

        ans = []
        per = [11] * len(nums)
        solve(nums, per, 0)
        return ans
