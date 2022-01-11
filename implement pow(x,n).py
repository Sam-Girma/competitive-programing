class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        test=n
        n=abs(n)
        def powe(x,n):
            if n==0:
                return 1
            else:
                if n%2==0:
                    ret=powe(x,n//2)
                    return ret*ret
                else:
                    ret=powe(x,n//2)
                    return x*ret*ret
        if test>=0:
            return powe(x,n)
        else:
            return 1/powe(x,n)
                    
            
            
            
