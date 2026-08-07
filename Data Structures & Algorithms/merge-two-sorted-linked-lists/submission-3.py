# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        prev = cur
        new = prev
        
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                cur = list2
                list2 = list2.next
            else:
                cur = list1
                list1 = list1.next

            prev.next = cur
            prev = cur

        last = list1 if list1 is not None else list2

        while last is not None:
            prev.next = last
            prev = last
            last = last.next

        return new.next