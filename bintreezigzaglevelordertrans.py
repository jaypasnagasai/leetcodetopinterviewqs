# 103. Binary Tree Zigzag Level Order Traversal

class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []

        res = [[root.val]]

        stack = [root]
        s = True
        height = []
        temp = []
        while stack:
            cur = stack.pop(0)

            if cur.left:
                temp.append(cur.left.val)
                height.append(cur.left)

            if cur.right:
                temp.append(cur.right.val)
                height.append(cur.right)

            if not s and temp and not stack:
                res.append(temp)
                s = True
                stack = height
                height = []
                temp = []

            elif s and temp and not stack:
                res.append(temp[::-1])
                s = False
                stack = height
                height = []
                temp = []
             
        return res
