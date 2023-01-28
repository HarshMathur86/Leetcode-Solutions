
""" Que ---> 
https://leetcode.com/problems/reverse-nodes-in-k-group/description/
"""

# Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        elements = []
        res_elements = []
        while(head != None):
            elements.append(head.val)
            head = head.next

        #print(elements)
        while(len(elements) >= k):
            #print("W")
            for num in elements[:k][::-1]:
                res_elements.append(num)
            elements = elements[k:]
        #print("RES->", res_elements)
        res_elements += elements
        #print("res --> ", res_elements)

        result_list_head = ListNode(res_elements[0])
        res_curr = result_list_head
        for ele in res_elements[1:]:
            res_curr.next = ListNode(ele)
            res_curr = res_curr.next

        return result_list_head
