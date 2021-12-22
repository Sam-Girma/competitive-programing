class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        lst=[]
        retlst=len(temperatures)*[0]
        for i in range (len(temperatures)):
            if len(lst)==0:
                lst.append(i)
            else:
                while len(lst)!=0 and temperatures[i]>temperatures[lst[-1]]:                  
                    retlst[lst.pop()] = i-lst[-1]
                lst.append(i)
        return retlst 
