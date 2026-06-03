from bisect import bisect_right

class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration
    ):
        
        def solve(firstStart, firstDur, secondStart, secondDur):
            rides = sorted(zip(secondStart, secondDur))

            starts = [s for s, d in rides]
            durations = [d for s, d in rides]

            n = len(rides)

            pref = [0] * n
            pref[0] = durations[0]

            for i in range(1, n):
                pref[i] = min(pref[i - 1], durations[i])

            suff = [0] * n
            suff[-1] = starts[-1] + durations[-1]

            for i in range(n - 2, -1, -1):
                suff[i] = min(
                    suff[i + 1],
                    starts[i] + durations[i]
                )

            ans = float('inf')

            for s, d in zip(firstStart, firstDur):
                T = s + d

                idx = bisect_right(starts, T)

                if idx > 0:
                    ans = min(ans, T + pref[idx - 1])

                if idx < n:
                    ans = min(ans, suff[idx])

            return ans

        return min(
            solve(landStartTime, landDuration,
                  waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration,
                  landStartTime, landDuration)
        )