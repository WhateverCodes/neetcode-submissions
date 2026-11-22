class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        if len(dict) < 2:
            return False
        forward, backward = {}, {}
        seen = set()
        base = sum(map(len, dict)) + 1
        for word in dict:
            m = len(word)
            prefix = [0] * (m + 1)
            suffix = [0] * (m + 1)
            for i, c in enumerate(word):
                key = (prefix[i], c)
                if key not in forward:
                    forward[key] = len(forward) + 1
                prefix[i + 1] = forward[key]
            for i in range(m - 1, -1, -1):
                key = (suffix[i + 1], word[i])
                if key not in backward:
                    backward[key] = len(backward) + 1
                suffix[i] = backward[key]
            for i in range(m):
                key = prefix[i] * base + suffix[i + 1]
                if key in seen:
                    return True
                seen.add(key)
        return False
