# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = 1

        def verifyBST(node: Optional[TreeNode], inf: int, sup: int) -> int:
            nonlocal res

            if res == -1:
                return -1

            if node is None:
                return 1

            if node.val >= sup or node.val <= inf:
                res = -1

            verifyBST(node.left, inf, node.val)
            verifyBST(node.right, node.val, sup)
            
            return 1

        verifyBST(root, float("-inf"), float("inf"))
        return res != -1
