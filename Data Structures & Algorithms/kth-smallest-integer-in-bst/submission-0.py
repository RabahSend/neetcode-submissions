# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []

        def addNode(node):
            nonlocal nodes

            if node is None:
                return

            nodes.append(node.val)

            addNode(node.left)
            addNode(node.right)

        addNode(root)
        nodes = sorted(nodes)

        return nodes[k - 1]