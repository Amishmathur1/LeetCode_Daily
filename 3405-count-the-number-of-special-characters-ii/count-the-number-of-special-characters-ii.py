class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            last_lower = word.rfind(ch)
            first_upper = word.find(ch.upper())

            if last_lower != -1 and first_upper != -1:
                if last_lower < first_upper:
                    count += 1

        return count