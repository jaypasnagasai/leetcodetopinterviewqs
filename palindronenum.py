# 9. Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False

        empty = []

        while x > 0:
            x, remd = divmod(x, 10)
            empty.append(remd)

        a=empty[::-1]
        if a==empty:
            return True
        
        else:
            return False
