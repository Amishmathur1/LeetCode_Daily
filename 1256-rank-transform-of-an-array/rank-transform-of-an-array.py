class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        d = {}

        ind = 1

        for i in sorted_arr:
            if i not in d:
                d[i] = ind
                ind += 1

        ans = []
        for num in arr:
            ans.append(d[num])
        return(ans)