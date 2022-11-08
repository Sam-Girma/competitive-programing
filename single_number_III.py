class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l = len(nums)

        res = nums[0]

        for i in range(1, l):
            res^=nums[i]

        count = 0
        while not res&1:
            res>>=1
            count+=1

        xor1, xor2 = None, None

        for i in range(0, l):
            temp = nums[i]>>count if count else nums[i]
            if temp&1:
                if xor1 is None:
                    xor1 = nums[i]
                else:
                    xor1^=nums[i]
            else:
                if xor2 is None:
                    xor2 = nums[i]
                else:
                    xor2^=nums[i]

        return [xor1, xor2]
