# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums, target):
        import bisect
        start=bisect.bisect_left(nums,target)      
        end=bisect.bisect_right(nums,target)
        if start>end-1:
            return [-1,-1]
        return [start,end-1]
