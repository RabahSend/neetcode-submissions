"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        copies = {}
        cur = head

        while cur is not None:
            copies[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur is not None:
            copies[cur].next = copies[cur.next] if cur.next is not None else None
            copies[cur].random = copies[cur.random] if cur.random is not None else None
            cur = cur.next

        return copies[head]
