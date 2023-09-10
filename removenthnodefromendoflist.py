# 19. Remove Nth Node From End of List

class Solution(object):
    def removeNthFromEnd(self, head, n):
        nodes = []
        temp = head
        while (temp):
            nodes.append(temp)
            temp = temp.next
        if (len(nodes)==1): return None
        if (len(nodes)-n<=0): return nodes[1]
        node = nodes[len(nodes)-1-n]
        node.next= node.next.next
        return head
