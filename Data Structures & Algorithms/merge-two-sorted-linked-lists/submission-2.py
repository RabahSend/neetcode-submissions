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

        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                cur = list2
                list2 = list2.next
            else:
                cur = list1
                list1 = list1.next

            prev.next = cur
            prev = cur

        while list1 is not None:
            prev.next = list1
            prev = list1
            list1 = list1.next

        while list2 is not None:
            prev.next = list2
            prev = list2
            list2 = list2.next

        return new.next