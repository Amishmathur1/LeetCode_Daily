class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, path):
            if start >= len(s):
                res.append(path[:])
                return

            for end in range(start+1, len(s)+1):
                x = s[start:end]
                if s[start:end] == x[::-1]:
                    path.append(s[start:end])
                    dfs(end, path)
                    path.pop()

        dfs(0, [])
        return (res)