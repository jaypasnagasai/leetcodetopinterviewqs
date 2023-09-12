# 300. Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums):
        ans = [nums.pop(0)]       
        for num in nums:           
            if num > ans[-1]:
                ans.append(num)
            else:
                ans[bisect_left(ans, num)] = num
                
        return len(ans)
