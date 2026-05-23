class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []

        for i in range(len(tokens)):

            if tokens[i].lstrip('-').isdigit():
                l.append(int(tokens[i]))

            else:

                b = l.pop()
                a = l.pop()

                if tokens[i] == '+':
                    l.append(a+b)

                if tokens[i] == '-':
                    l.append(a-b)

                if tokens[i] == '*':
                    l.append(a*b)

                if tokens[i] == '/':
                    l.append(int(a/b))

        

        return (l[-1])