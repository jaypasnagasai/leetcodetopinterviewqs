# 134. Gas Station

class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gain = 0
        curr_gain = 0
        answer = 0
        
        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1
        
        return answer if total_gain >= 0 else -1
