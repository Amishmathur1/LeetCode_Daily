class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # s = "hi(name)"
        # knowledge = [["a","b"]]
        
        result = re.findall(r'\([^)]*\)|[a-zA-Z]+', s)

        d = defaultdict(str)
        for i, j in knowledge:
            i = '('+i+')'
            d[i] = j


        for ind in range(len(result)):
            if result[ind] in d:
                result[ind] = d[result[ind]]
            elif result[ind] not in d and result[ind][0] == '(' and result[ind][-1] == ')':
                result[ind] = '?'

        return "".join(result)