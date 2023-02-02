# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        start = head
        while start is not None:
            length += 1
            start = start.next
        if length == 1:
            return None
        # node pos(index) from start
        pos = length - n
        start = head
        if pos == 0:
            return head.next
        for i in range(length):
            print(start.val)
            if i == pos-1:
                start.next = start.next.next
                break
            start = start.next
            
        return head
