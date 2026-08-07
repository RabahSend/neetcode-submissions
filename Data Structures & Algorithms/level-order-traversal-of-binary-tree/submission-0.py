# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        levels = []
        queue = deque([root])

        while len(queue) > 0:
            actual_lvl = len(queue)
            nodes_level = []

            for i in range(actual_lvl):
                node = queue.popleft()
                nodes_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            levels.append(nodes_level)

        return levels
