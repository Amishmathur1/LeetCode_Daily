class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # Making Adjacency List
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if i not in graph:
                graph[i] = []

        #########################

        visited = set()
        count = 0
        

        def bfs(node):
            dq = deque([node])
            component = []

            while dq:
                node = dq.popleft()
                component.append(node)

                for i in graph[node]:
                    if i not in visited:
                        visited.add(i)
                        dq.append(i)
            return component

        for i in range(n):
            if i not in visited:
                visited.add(i)
                component = bfs(i)

                k = len(component)
                pikachu = True

                for i in component:
                    if len(graph[i]) != k-1:
                        pikachu = False
                        break
                if pikachu:
                    count += 1

        return (count)