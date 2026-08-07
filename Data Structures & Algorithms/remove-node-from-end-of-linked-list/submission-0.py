# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
   
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next

        if slow.next is None:
            slow = None
        else:
            slow.next = slow.next.next

        return dummy.next
