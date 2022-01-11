class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def calc(nums,start,end):
            if start==end:
                return nums[start]
            else:
                return max(nums[start]-calc(nums,start+1,end),nums[end]-calc(nums,start,end-1))
        score=calc(nums,0,len(nums)-1)
        
        if score>=0:
            return True
        else:
            return False
        
