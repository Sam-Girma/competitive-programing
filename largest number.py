class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        result=""
        for i in range (len(nums)):
            for j in range (len(nums)-1):
                if (int(str(nums[j])+str(nums[j+1])))<int(str(nums[j+1])+str(nums[j])):
                                                    nums[j+1],nums[j]=nums[j],nums[j+1]

        result = "".join(list(map(str, nums)))
        if int(result)==0:
            result="0"
        return result
