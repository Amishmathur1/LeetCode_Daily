class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        remove = length - n

        # removing the first node
        if remove == 0:
            return head.next

        prev = None
        temp = head
        pos = 0

        while pos < remove:
            prev = temp
            temp = temp.next
            pos += 1

        prev.next = temp.next

        return head