# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree_merger(root1, root2):
        if root1 is None and root2 is None:
            return None
        elif root1 is None:
            return root2
        elif root2 is None:
            return root1

        merged_tree = TreeNode(val = root1.val + root2.val)
        merged_tree.left = Solution.tree_merger(root1.left, root2.left)
        merged_tree.right = Solution.tree_merger(root1.right, root2.right)

        return merged_tree


    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        result = Solution.tree_merger(root1, root2)
        return result