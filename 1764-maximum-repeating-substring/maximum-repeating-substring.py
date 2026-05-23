class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        count = 1
        while True:            
            if word*count in sequence:
                k += 1
                count += 1
            else:
                return k