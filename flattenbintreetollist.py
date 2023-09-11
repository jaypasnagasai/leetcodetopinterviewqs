# 114. Flatten Binary Tree to Linked List

class Solution:
    def flatten(self, root):
        def solve(root):
            if not root:
                return None
            
            leftTail = solve(root.left)
            rightTail = solve(root.right)
            
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            
            tail = rightTail or leftTail or root
            return tail
        
        solve(root)
