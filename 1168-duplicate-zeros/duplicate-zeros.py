class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        x = len(arr)
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1, 0)
                i += 2
            else:
                i += 1
        
        y = len(arr) - x
        for i in range(y):
            arr.pop()

