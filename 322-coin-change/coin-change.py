class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dq = deque([amount])
        coins_needed = 0
        visited = {amount}

        while dq:
            size = len(dq)
            coins_needed += 1

            for _ in range(size):
                value = dq.popleft()
                for j in coins:
                    new_val = value - j

                    if new_val == 0:
                        return coins_needed

                    if new_val > 0 and new_val not in visited:
                        dq.append(new_val)
                        visited.add(new_val)
        return -1
