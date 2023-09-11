# 86. Partition List

class Solution:
  def partition(self, head, x):
    small_head = small = ListNode(-1)
    large_head = large = ListNode(-1)

    while head:
      if head.val < x:
        small.next = head
        small = small.next
      else:
        large.next = head 
        large = large.next
      head = head.next
    
    large.next = None
    small.next = large_head.next
    return small_head.next
