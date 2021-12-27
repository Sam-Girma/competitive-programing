class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        while(i!=(len(intervals)-1)):
            if intervals[i][1]>=intervals[i+1][0]:
                if intervals[i][1]<=intervals[i+1][1]:
                    intervals[i]=[intervals[i][0],intervals[i+1][1]]
                    del intervals[i+1]
                    continue
                else:
                    del intervals[i+1]
                    continue
            i+=1
                    
                
        return intervals
        
