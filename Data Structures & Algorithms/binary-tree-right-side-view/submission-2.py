# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        queue = deque([root])

        while queue:
            level = len(queue)

            for i in range(level):
                node = queue.popleft()

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

                if i == level - 1:
                    res.append(node.val)

        return res

                