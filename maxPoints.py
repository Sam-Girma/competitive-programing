
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        max_points = 0
        for point in points:
            slopes = defaultdict(int)
            for point2 in points:
                if point == point2:
                    continue
                if point2[0]==point[0]:
                    slopes["vert"]+=1
                else:
                    slopes[(point[1]-point2[1])/(point[0]-point2[0])]+=1
            max_points = max(max_points, 1+max(slopes.values()))
        return max_points
