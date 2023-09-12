# 201. Bitwise AND of Numbers Range

class Solution:
    def rangeBitwiseAnd(self, left, right):
        check, dist = right & left, right-left
        for i in range(31, -1, -1):
            if check & (1 << i) and (1 << i) < dist: 
                check = check & ~(1<<i)
        return check
