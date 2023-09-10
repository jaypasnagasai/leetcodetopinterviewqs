# 28. Find the Index of the First Occurrence in a String

class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        
        if m == 0:
            return 0 
        
        for i in range(n - m + 1):
            found = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        return -1  
