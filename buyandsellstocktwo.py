# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, p):
        pro = 0
        for i in range (1, len (p)):
            if p[i] > p[i-1]:
                pro += p[i] - p[i-1]
        return pro
