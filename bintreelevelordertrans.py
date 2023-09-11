# 102. Binary Tree Level Order Traversal

from collections import deque

class Solution:
    def levelOrder(self, root):
        result = []
        if not root:
            return result

        # Initialize a queue with the root node
        queue = deque([root])

        # Perform level-order traversal
        while queue:
            level_values = []
            level_size = len(queue)
            for _ in range(level_size):
                # Process the next node in the queue
                node = queue.popleft()
                level_values.append(node.val)
                
                # Enqueue the left child if it exists
                if node.left:
                    queue.append(node.left)
                
                # Enqueue the right child if it exists
                if node.right:
                    queue.append(node.right)
            
            # Add the values of the current level to the result
            result.append(level_values)
        
        # Return the final level-order traversal result
        return result
