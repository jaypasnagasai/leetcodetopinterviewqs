# 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n):
        res=[]
        
        def BackTracking(CurString,openC,closeC):
            if len(CurString)==2*n:
                res.append(CurString)
                return
            if openC<n:
                BackTracking(CurString+"(",openC+1,closeC)
            if closeC<n and openC>closeC:
                BackTracking(CurString+")",openC,closeC+1)
        
        BackTracking("",0,0)
        
        return res
            
