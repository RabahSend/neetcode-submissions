# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root
        
        def findLCA(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            nonlocal lca

            if root is None:
                return None

            sup = max(p.val, q.val)
            inf = min(p.val, q.val)    

            if root.val < inf:
                findLCA(root.right, p, q)
            elif root.val > sup:
                findLCA(root.left, p, q)
            else:
                lca = root


        findLCA(root, p, q)

        return lca