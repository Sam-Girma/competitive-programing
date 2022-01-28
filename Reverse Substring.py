class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        counter=0
        returnedString=""
        for i in s:
            if i!=")":
                stack.append(i)
                counter+=1
            else:
                a=""
                counter+=1
                while(stack[-1]!="("):
                    a+=stack.pop()
                stack.pop()
                if len(stack)==0 and counter==len(s):
                    return a
                else:
                    for i in a:
                        stack.append(i)
        for i in range(len(stack)):
            returnedString+=stack.pop(0)
        return returnedString
        
