class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        x = moves.count('L') + moves.count('_') - moves.count('R')
        y = moves.count('R') + moves.count('_') - moves.count('L')
        return max(x,y)