class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        r = 0
        for i in range(1, len(points)):
            a = abs(points[i][0] - points[i-1][0])
            b = abs(points[i][1] - points[i-1][1])
            r += max(a, b)
        return r
