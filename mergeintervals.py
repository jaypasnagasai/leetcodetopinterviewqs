# 56. Merge Intervals

class Solution(object):
    def merge(self, intervals):
        intervals=sorted(intervals, key=lambda x:x[0])
        l=len(intervals)-1
        i=0
        while(i<l):
            if(intervals[i][1]>=intervals[i+1][0] and intervals[i][1]<=intervals[i+1][1]):
                arr=[intervals[i][0],intervals[i+1][1]]
                intervals.remove(intervals[i])
                intervals.remove(intervals[i])
                intervals.insert(i,arr)
                l-=1
                i-=1
            elif(intervals[i][1]>=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]):
                intervals.remove(intervals[i+1])
                l-=1
                i-=1      
            i+=1
        return intervals
