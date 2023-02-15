# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        contents = []
        for head in lists:
            while head is not None:
                contents.append(head.val)
                head = head.next
        
        if len(contents) == 0:
            return None
        contents.sort()
        head = ListNode(val=contents[0])
        if len(contents) == 1:
            return head
        node = head
        for ele in contents[1:]:
            node.next = ListNode(ele)
            node = node.next

        return head