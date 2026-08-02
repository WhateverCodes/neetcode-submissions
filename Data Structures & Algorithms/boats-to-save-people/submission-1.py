class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        s = 0
        e = len(people)-1
        while s < e :
            if people[s]+people[e] > limit :
                ans += 1
                e -= 1
            else :
                ans += 1
                s += 1
                e -= 1
        if s == e : ans += 1
        return ans