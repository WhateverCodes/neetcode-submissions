class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows) :
            if i == 0 : ans.append([1])
            elif i == 1 : ans.append([1, 1])
            else :
                t = [1]
                k = ans[-1]
                for j in range(i-1) : t.append(k[j] + k[j+1])
                t.append(1)
                ans.append(t)
        return ans