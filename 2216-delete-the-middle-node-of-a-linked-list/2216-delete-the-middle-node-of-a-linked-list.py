# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head 
        prev = None
        if slow.next is None:
            return prev

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        nxt = slow.next
        prev.next = nxt

        return head
        