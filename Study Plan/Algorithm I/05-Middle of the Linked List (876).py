# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Calculating length
        l = 0
        h = head
        while h is not None:
            l += 1
            h = h.next
        mid = l//2
        mid_node = head
        for _ in range(mid):
            mid_node = mid_node.next
        return mid_node
