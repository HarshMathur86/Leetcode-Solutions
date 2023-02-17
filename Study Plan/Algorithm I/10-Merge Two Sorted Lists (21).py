# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lst = []
        while list1 != None:
            lst.append(list1.val)
            list1 = list1.next
        while list2 != None:
            lst.append(list2.val)
            list2 = list2.next
        #print(lst)
        lst.sort()
        #print(lst)
        merged_list = ListNode()
        head = merged_list
        try:
            head.val = lst[0]
        except:
            head = None
            return head
        for val in lst[1:]:
            merged_list.next = ListNode()
            merged_list = merged_list.next
            merged_list.val = val
        return head