class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt={}
        retlst=[]
        lst=[]
        for i in nums:
            dictt[i]=0
        for i in range(len(nums)):
            dictt[nums[i]]+=1
        
        for i in dictt:
            lst.append([dictt[i],i])
            
        lst.sort()
        
        
        for i in range(k):
            retlst.append(lst.pop()[1])
        
            
        return retlst
        
