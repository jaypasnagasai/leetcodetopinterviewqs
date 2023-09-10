# 138. Copy List with Random Pointer

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        node_map = {}
        current = head
        
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        current = head
        
        while current:
            copy_node = node_map[current]
            copy_node.next = node_map.get(current.next)
            copy_node.random = node_map.get(current.random)
            current = current.next
        
        return node_map[head]
