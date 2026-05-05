# Definition for singly-linked list.
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        greater = ListNode(0)
        lesser = ListNode(0)

        great = greater
        less = lesser

        temp = head
        while temp:
            if temp.val < x:
                less.next = temp
                less = less.next

            else:
                great.next = temp
                great = great.next

            temp = temp.next

        great.next = None

        less.next = greater.next
        return lesser.next