# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # Case 1: duplicate sequence detected
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val

                # skip all nodes with this value
                while curr and curr.val == dup_val:
                    curr = curr.next

                prev.next = curr   # reconnect after duplicates

            # Case 2: no duplicate
            else:
                prev = curr
                curr = curr.next

        return dummy.next