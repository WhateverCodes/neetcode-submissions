class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        can = 0
        l = len(flowerbed)
        for i in range(l) :
            if flowerbed[i] == 0 :
                if (i == 0 or flowerbed[i-1] == 0) and (i == l-1 or flowerbed[i+1] == 0) :
                    can += 1
                    flowerbed[i] = 1
        return n <= can