# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        temp = head
        n = 1 #Length of the linkedlist

        while temp.next:
            temp = temp.next
            n += 1

        last = temp

        #making the list circular
        last.next = head
        
        k = k % n
        temp = head
        steps = n - k

        for _ in range(steps - 1):
            temp = temp.next

        new_head = temp.next
        temp.next = None

        return new_head