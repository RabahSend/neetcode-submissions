# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def height(root: Optional[TreeNode]) -> int:
            nonlocal best

            if root is None:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)

            best = max(best, left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)

        return best