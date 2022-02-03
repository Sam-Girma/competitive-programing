class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        answer=[]
        for k in range(len(l)):
            todo=nums[l[k]:r[k]+1]
            todo.sort()
            if len(todo)==1:
                answer.append(False)
                continue
            if len(todo)==2:
                answer.append(True)
                continue
            diff=todo[1]-todo[0]
            for i in range(2,len(todo)):
                if diff!=todo[i]-todo[i-1]:
                    answer.append(False)
                    break
                if i==(len(todo)-1):
                    answer.append(True)
        return answer
        
        
