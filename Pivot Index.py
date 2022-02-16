class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Lsum=[0]
        Rsum=[0]
        if len(nums)==0:
            return -1
        for i in range(len(nums)-1):
            Lsum.append(Lsum[-1]+nums[i])
        for j in range(len(nums)-1,0,-1):
            Rsum.append(Rsum[-1]+nums[j])
        Rsum.reverse()
        for i in range(len(Lsum)):
            if Lsum[i]==Rsum[i]:
                return i            
        return -1
