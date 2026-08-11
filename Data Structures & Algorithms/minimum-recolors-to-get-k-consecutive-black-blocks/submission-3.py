class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        return min(blocks[i-k:i].count('W') for i in range(k, len(blocks) + 1))