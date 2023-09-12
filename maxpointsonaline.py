# 149. Max Points on a Line

class Solution(object):
    def maxPoints(self, points):
        count = len(points)
        if count < 3:
            return count
        result = 2
        for i, p1 in enumerate(points[:-1]):
            data = {}
            for p2 in points[i+1:]:
                a = None
                x = p2[0] - p1[0]
                if x:
                    a = (1.0*p2[1] - p1[1]) / x
                if a in data:
                    new = data[a] = data[a] + 1
                    if new > result:
                        result = new
                else:
                    data[a] = 2
        return result
