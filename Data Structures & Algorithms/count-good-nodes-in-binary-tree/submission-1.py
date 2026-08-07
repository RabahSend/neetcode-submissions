# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxi = root.val
        
        def path(root: TreeNode, maxi: int) -> int:
            if root is None:
                return 0

            if root.val >= maxi:
                maxi = root.val
                val = 0
                if root.left is not None:
                    val += path(root.left, maxi)
                if root.right is not None:
                    val += path(root.right, maxi)

                return 1 + val
                    
            return 0 + path(root.left, maxi) + path(root.right, maxi)
            
        return path(root, maxi)
