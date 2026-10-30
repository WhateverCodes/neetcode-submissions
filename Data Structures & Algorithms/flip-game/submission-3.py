class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ans = []
        for i in range(len(currentState) - 1):
            if currentState[i] == '+' and currentState[i + 1] == '+':
                t = currentState[:i] + '--' + currentState[i + 2:]
                ans.append(t)
        return ans