class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if edges == []:
            return True
        d = defaultdict(list)
        for r, c in edges:
                d[r].append(c)
                d[c].append(r)

        dq = deque([source])
        seen = set()
        while dq:
                node = dq.popleft()
                l = d[node]
                for i in l:
                    if i == destination:
                        return True
                    if i not in seen:
                        seen.add(i)
                        dq.append(i)

        return False