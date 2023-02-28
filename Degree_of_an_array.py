class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
    	frequency = {}
    	for index, num in enumerate(nums):
    		if num in frequency: frequency[num].append(index)
    		else: frequency[num] = [index]
    	maximum_degree = max([len(i) for i in frequency.values()])
    	return min([i[-1]-i[0]+1 for i in frequency.values() if len(i) == maximum_degree])
		
		
