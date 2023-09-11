# 98. Validate Binary Search Tree

class Solution:
    def isValidBST(self, root):
        def valid_bst(root, min_val, max_val):
            if root is None:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return valid_bst(root.left, min_val, root.val) and valid_bst(root.right, root.val, max_val)
        return valid_bst(root, -2**31-1, 2**31)
