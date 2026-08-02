class Solution:
    def reverseWords(self, s: List[str]) -> None:
        b = 0
        n = len(s)
        e = n - 1
        while b < e:
            s[b], s[e] = s[e], s[b]
            b += 1
            e -= 1
        start = 0
        while start < n:
            end = start
            while end < n and s[end] != ' ':
                end += 1
            l = start
            r = end-1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            start = end + 1