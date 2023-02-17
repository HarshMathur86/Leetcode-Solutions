# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elements = []
        while head is not None:
            elements.append(head.val)
            head = head.next
        
        elements.reverse()
        res_node = ListNode(elements[0])
        curr = res_node
        
        for e in elements[1:]:
            curr.next = ListNode(e)
            curr = curr.next
            
        return res_node