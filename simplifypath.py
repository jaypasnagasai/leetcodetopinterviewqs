# 71. Simplify Path

class Solution:
    def simplifyPath(self, path):
        return '/'+'/'.join(reduce(lambda r,p:(r+[p][p in'.':],r[:-1])[p=='..'],path.split('/'),[]))
