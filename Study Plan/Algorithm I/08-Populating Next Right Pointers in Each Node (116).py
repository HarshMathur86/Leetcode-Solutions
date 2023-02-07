"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connector(left_child, right_child):
        if left_child is None:
            return

        left_child.next = right_child
        
        Solution.connector(left_child.left, left_child.right)
        Solution.connector(left_child.right, right_child.left)
        Solution.connector(right_child.left, right_child.right)
        
        
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        Solution.connector(root.left, root.right)
        return root
