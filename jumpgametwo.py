# 45. Jump Game II

class Solution:
    def jump(self, nums):

        x = [nums[i]+i for i in range(len(nums))]  
        l,r,jumps = 0,0,0

        while r < len(nums)-1 :
            jumps += 1
            l,r = r+1,max(x[l:r+1]) 

        return jumps
