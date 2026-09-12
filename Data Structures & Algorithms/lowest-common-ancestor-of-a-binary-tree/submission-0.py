# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if node is None:
                return None

            if node == p or node == q:
                return node

            leftInfo = dfs(node.left)
            rightInfo = dfs(node.right)

            if leftInfo is not None:
                if rightInfo is not None:
                    return node

                return leftInfo

            return rightInfo

        return dfs(root)            