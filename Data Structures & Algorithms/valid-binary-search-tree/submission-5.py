# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def path(root, borderMin, borderMax):
            if root is None:
                return True

            if root.val <= borderMin or root.val >= borderMax:
                return False

            return path(root.left, borderMin, root.val) and path(root.right, root.val, borderMax)

        return path(root, float("-inf"), float("inf"))
