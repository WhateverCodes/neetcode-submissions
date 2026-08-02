class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for p in operations :
            if p == '+' : points.append(points[-1]+points[-2])
            elif p == 'C' : points.pop()
            elif p == 'D' : points.append(2*points[-1])
            else : points.append(int(p))
        return sum(points)