# 129. Sum Root to Leaf Numbers

class Solution(object):
    def sumNumbers(self, root):        
        def isLeaf(node):
            if node is None:
                return False
            elif node.left is None and node.right is None:
                return True
            return False
        lst = []
        def dfs(node, sum):
            if node is None:
                return 
            elif isLeaf(node):
                lst.append(10*sum+node.val)
            dfs(node.left, 10*sum+node.val)
            dfs(node.right, 10*sum+node.val)
        dfs(root, 0)
        return sum(lst)
