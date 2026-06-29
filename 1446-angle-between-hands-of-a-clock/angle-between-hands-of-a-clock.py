class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        return min(((11 * (hour + minutes / 60)) % 12), 12 - ((11 * (hour + minutes / 60)) % 12)) * 30