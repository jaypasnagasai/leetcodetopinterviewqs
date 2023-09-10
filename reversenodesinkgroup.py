# 25. Reverse Nodes in k-Group

class Solution:
    def reverseKGroup(self, head, k):
        count=0
        temp=head
        while temp:
            temp=temp.next
            count+=1
        n=count//k
        prev=dummy=ListNode()
        dummy.next=head
        while n:
            curr=prev.next
            nex=curr.next
            for i in range(1,k): 
                curr.next=nex.next
                nex.next=prev.next
                prev.next=nex
                nex=curr.next
            prev=curr
            n-=1
        return dummy.next
