class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)-1):
            if (nums[i]>nums[i-1]) and (nums[i]<nums[i+1]):
                nums[i],nums[i+1]=nums[i+1],nums[i]
            elif(nums[i]<nums[i-1]) and (nums[i]>nums[i+1]):
                nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums
        
