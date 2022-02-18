class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        changed.sort()
        check=defaultdict(int)
        orginal=[]
        for nums in range(len(changed)):
            check[changed[nums]]+=1
        
        for i in range(len(changed)):
            num=changed[-i-1]
            if check[num]==0:
                continue
            elif num%2!=0:
                return []
            else:
                check[num]-=1
                check[num//2]-=1
                orginal.append(num//2)
        
        if len(orginal)==(len(changed)//2):
            return orginal
        else:
            return []
