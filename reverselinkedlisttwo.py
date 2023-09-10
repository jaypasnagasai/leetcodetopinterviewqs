# 92. Reverse Linked List II

class Solution:
    def reverseBetween(self,head,left,right):
        dummy=ListNode(0)
        dummy.next=head

        prev=dummy
        cur=dummy.next

        for i in range(1,left):
            cur=cur.next
            prev=prev.next


        for i in range(right-left):
            temp=cur.next
            cur.next=temp.next
            temp.next=prev.next
            prev.next=temp    


        return dummy.next    
