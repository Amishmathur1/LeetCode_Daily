class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, tuple(points[0]))]
        visited = set()
        total_sum = 0

        while heap:
            dis, node = heappop(heap)
            
            if node in visited:
                continue

            visited.add(node)
            total_sum += dis

            for i in points:
                if tuple(i) not in visited:
                    distance = (abs(node[0] - i[0]) + abs(node[1] - i[1]))
                    heappush(heap,(distance, (tuple(i))))

        return (total_sum)