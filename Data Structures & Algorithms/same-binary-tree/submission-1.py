# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def compare(root_p: Optional[TreeNode], root_q: Optional[TreeNode]) -> int:
            if root_p == None and root_q == None:
                return 0

            if (root_p == None and root_q != None) or (root_p != None and root_q == None):
                return -1

            if root_p.val != root_q.val:
                return -1

            comparison_left = compare(root_p.left, root_q.left)
            if comparison_left == -1:
                return -1

            comparison_right = compare(root_p.right, root_q.right)
            if comparison_right == -1:
                return -1

            return 1

        return compare(p, q) != -1

            