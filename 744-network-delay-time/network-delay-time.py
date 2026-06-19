from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))
        
        min_time = {}
        min_heap = [(0,k)]

        while min_heap:
            curr_time, i = heappop(min_heap)
            if i in min_time:
                continue
            
            min_time[i] = curr_time
            for nei, nei_time in graph[i]:
                if nei not in min_heap:
                    heappush(min_heap, (curr_time + nei_time, nei))
        

        if len(min_time) == n:
            return max(min_time.values())
        else:
            return -1
