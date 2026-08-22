class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        t = 0
        l = 0
        r = 0
        ans = 0
        ts = threshold * k
        while r < len(arr) :
            t += arr[r]
            if r - l + 1 == k:
                if t >= ts:
                    ans += 1
                t -= arr[l]
                l += 1
            r += 1
        return ans