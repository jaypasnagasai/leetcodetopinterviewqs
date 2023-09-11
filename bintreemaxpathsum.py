# 124. Binary Tree Maximum Path Sum

class Solution:
    def maxPathSum(self, root):
        self.ans = -sys.maxsize
        
        def dfs(node):
            if not node: return 0
			
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(node.val + left + right, self.ans)
            return max(0, max(left + node.val, right + node.val))
        dfs(root)
        return self.ans
