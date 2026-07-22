class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for i in strs:
            x = ''.join(sorted(i))
            d[x].append(i)
        l = list(d.values())
        return l[::-1]