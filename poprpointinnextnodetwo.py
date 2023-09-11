# 117. Populating Next Right Pointers in Each Node II

from collections import deque

class Solution:
  def connect(self, root):
    if root is None:
        return None
    q = deque([root])
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i < level_size - 1:
                node.next = q[0]
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
    return root
