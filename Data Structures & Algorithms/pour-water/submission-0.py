class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        heights = heights[:]
        for _ in range(volume):
            best = k
            i = k - 1
            while i >= 0 and heights[i] <= heights[i + 1]:
                if heights[i] < heights[best]:
                    best = i
                i -= 1
            if best == k:
                i = k + 1
                while i < len(heights) and heights[i] <= heights[i - 1]:
                    if heights[i] < heights[best]:
                        best = i
                    i += 1
            heights[best] += 1
        return heights
