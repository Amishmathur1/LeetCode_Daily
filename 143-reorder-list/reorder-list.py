# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return []

        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        mid = ceil(len(nums) / 2)
        arr1 = nums[:mid]
        arr2 = nums[mid:]
        arr2 = arr2[::-1]
        print(arr1, arr2)

        l1 = l2 = 0
        check = 1
        ans = []
        while l1 < mid:
            if check % 2 != 0:
                ans.append(arr1[l1])
                l1 += 1
            else:
                ans.append(arr2[l2])
                l2 += 1
            check += 1
        
        if l2 < len(arr2):
            ans.append(arr2[l2])
        
        curr = head
        for i in ans:
            curr.val = i
            curr = curr.next