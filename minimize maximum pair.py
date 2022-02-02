class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sums=[]
        for i in range(len(nums)//2):
            sums.append(nums[i]+nums[-i-1])
        return max(sums)
            
