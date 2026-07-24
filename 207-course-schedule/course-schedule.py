class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        #Creating Indegree list
        ind = [0] * numCourses
        print(graph)

        for i in range(numCourses):
            for nei in graph[i]:
                ind[nei] += 1

        print(ind)

        #Checking for nei
        dq = deque([])
        count  = 0
        for i in range(len(ind)):
            if ind[i] == 0:
                dq.append(i)
        print(dq)

        while dq:
            val = dq.popleft()
            count += 1
            for nei in graph[val]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    dq.append(nei)

        if count == numCourses:
            return (True)
        else:
            return (False)
