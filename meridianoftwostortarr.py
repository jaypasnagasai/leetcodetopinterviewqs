# 4. Median of Two Sorted Arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = sorted(nums1+nums2)
        if len(nums3) % 2 == 1:
            return nums3[len(nums3)/2]
        else:
            return (nums3[len(nums3)/2] + nums3[len(nums3)/2-1]) / 2.0
