class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def mine(n):
            if n==1:
                return True
            if n==0:
                return False
            else:
                if n%3==0:
                    return mine(n//3)
                else:
                    
                    return False
        return mine(n)
        
