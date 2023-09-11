# 230. Kth Smallest Element in a BST

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse(self, root):
        if root:
            self.traverse(root.left)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
                return
            self.traverse(root.right)
            
    def kthSmallest(self, root, k):
        self.k = k
        self.traverse(root)
        return self.ans
