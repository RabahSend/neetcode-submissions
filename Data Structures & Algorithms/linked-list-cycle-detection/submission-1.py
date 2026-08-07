# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_pointer = head
        slow_pointer = head

        while head is not None:
            if fast_pointer is None or fast_pointer.next is None:
                return False

            fast_pointer = (fast_pointer.next).next

            if fast_pointer == slow_pointer:
                return True

            slow_pointer = slow_pointer.next

            head = head.next

        return False
