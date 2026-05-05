# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = head.next

        curr = head
        prev = None

        while curr and curr.next:
            first = curr
            second = curr.next

            first.next = second.next
            second.next = first

            if prev:
                prev.next = second

            prev = first
            curr = first.next

        return new_head