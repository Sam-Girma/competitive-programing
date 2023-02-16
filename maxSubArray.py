class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            maxim = max(dp[-1] + nums[i], nums[i]) if dp else nums[i]
            dp.append(maxim)
        return max(dp)
