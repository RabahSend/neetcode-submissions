# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def verify(root, p, q):
            if root.val > q.val:
                return verify(root.left, p, q)
            elif root.val < p.val:
                return verify(root.right, p, q)
            else:
                return root

        if p.val > q.val:
            q, p = p, q
        return verify(root, p, q)