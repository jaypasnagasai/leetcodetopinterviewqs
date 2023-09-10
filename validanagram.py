# 242. Valid Anagram

class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        arr1 = {}
        arr2 = {}
        for i in s:
            if i in arr1:
                arr1[i]+=1
               
            else:
                arr1[i] = 1
        for j in t:
            if j in arr2:
                arr2[j]+=1
               
            else:
                arr2[j] = 1
        print(arr1,arr2)
        if arr1 == arr2:
            return True
        return False
