class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maximum_difference = -1
        minimum = nums[0]
        for i in range(1, len(nums)):
            maximum_difference = max(maximum_difference, nums[i]-minimum)
            minimum = min(minimum, nums[i])
        return -1 if maximum_difference==0 else maximum_difference
