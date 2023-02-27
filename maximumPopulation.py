class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        maximum = [float("-inf"), 0]

        for i in range(1000):
            count = 0
            for year in logs:
                if year[0]<=1950+i<year[1]:
                    count+=1
            if count>maximum[0]:
                maximum[0] = count
                maximum[1] = 1950+i
        return maximum[1]
