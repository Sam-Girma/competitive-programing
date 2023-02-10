class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [nums[0]*nums[0]]
        
        squarearr=[]
        nums=deque(nums)
        i=0
        leng=len(nums)
        while(len(squarearr)<leng):
            a=nums[0]
            b=nums[-1]
            if (a*a>=b*b):
                squarearr.append(a*a)
                nums.popleft()
            else:
                squarearr.append(b*b)
                nums.pop()
        squarearr.reverse()
        return squarearr
                
            
        
    
        
