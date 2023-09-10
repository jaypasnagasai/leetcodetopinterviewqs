# 274. H-Index

class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True) 
        n = len(citations)
        h = 0
        for i in range(n):
            if citations[i] >= i+1: 
                h = i+1 
        return h
