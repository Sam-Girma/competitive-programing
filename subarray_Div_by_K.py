class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = defaultdict(int)
        prefix = [nums[0]]
        ans = 0
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        for ele in prefix:
            remainders[ele%k]+=1
            if ele%k ==0 :
                ans+=1
        for i in remainders:
            if remainders[i]>1:
                ans+=(remainders[i]*(remainders[i]-1)//2)
        return ans
