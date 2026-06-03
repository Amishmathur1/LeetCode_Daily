class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = Counter(secret)

        countA = 0
        countB = 0
        k = []
        print(d)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                countA += 1
                d[str(secret[i])] -= 1
                print("SAME",d)
                
        for i in range(len(secret)):
            if secret[i] != guess[i] and d[guess[i]] > 0:
                countB += 1
                d[guess[i]] -= 1
            
        print(d)
        ans = str(countA) + 'A' + str(countB) + 'B'
        return (ans)