class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]          # Save original value
            arr[i] = rightMax      # Replace with max to its right
            rightMax = max(rightMax, curr)  # Update running maximum

        return arr