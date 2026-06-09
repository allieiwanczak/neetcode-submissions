# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle by using slow and fast pointers
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse starting from slow.next
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # combine
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
