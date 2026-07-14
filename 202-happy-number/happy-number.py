class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        new_num = str(n)

        while 1:
            x = 0
            for i in new_num:
                x += int(i) ** 2

            if x == 1:
                return True

            if x in visited:
                return False

            visited.add(x)
            new_num = str(x)
