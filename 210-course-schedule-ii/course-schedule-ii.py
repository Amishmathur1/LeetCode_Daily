class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        ind = [0]*numCourses
        ans = []
        for u,v in prerequisites:
            adj[u].append(v)
            ind[v] +=1
        q = deque([i for i in range(numCourses) if ind[i]==0])
        while q:
            curr = q.popleft()
            ans.append(curr)
            for n in adj[curr]:
                ind[n] -=1
                if ind[n]==0:
                    q.append(n)
        if len(ans) == numCourses:
            return ans[::-1]
        return []