class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        retarr=[]
        def myFunc(points):
            return sqrt((points[0]*points[0])+(points[1])*(points[1]))
        
        points.sort(key=myFunc)
         for i in range(k):
            retarr.append(points[i])
        return retarr
        
