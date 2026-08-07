# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,  Llist: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head = Llist

        while Llist is not None:
            next_n = cur.next
            cur.next = prev
            prev = cur
            Llist = next_n
            cur = Llist

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None

        second = self.reverse(second)
        first = head

        while second is not None:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            second = second_next
            first = first_next




