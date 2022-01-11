class Solution(object):
    def isPowerOfFour(self, n):
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
                if n%4==0:
                    return mine(n//4)
                else:
                    
                    return False
        return mine(n)
