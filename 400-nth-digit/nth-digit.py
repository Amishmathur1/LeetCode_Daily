class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        # Step 1: Find digit length group
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # Step 2: Identify the exact number
        start += (n - 1) // length

        # Step 3: Find the digit inside that number
        idx = (n - 1) % length
        return int(str(start)[idx])