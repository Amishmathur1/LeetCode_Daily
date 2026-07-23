from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites, queries):

        adj = defaultdict(list)
        ind = [0] * numCourses

        for u, v in prerequisites:
            adj[u].append(v)
            ind[v] += 1

        q = deque([i for i in range(numCourses) if ind[i] == 0])
        pre = [set() for _ in range(numCourses)]

        while q:
            curr = q.popleft()

            for nei in adj[curr]:
                pre[nei].add(curr)
                pre[nei].update(pre[curr])

                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)

        return [u in pre[v] for u, v in queries]