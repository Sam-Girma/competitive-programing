class Solution:
    def isValid(self, s: str) -> bool:
        dictt={'(':')','{':'}','[':']'}
        lst=[]
        for i in s:
            if i in dictt.keys():
                lst.append(i)
            else:
                
                if len(lst)==0:
                    return False
                elif dictt[lst[-1]]==i:
                    lst.pop()
                else: return False
        if len(lst)==0:
            return True
        else: return False
                
        
