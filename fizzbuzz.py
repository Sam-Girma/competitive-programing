class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lis = []
        
        for i in range (1,n+1):
            div_3 = (i%3==0)
            div_5 = (i%5==0)
            
            if div_3 and div_5:
                lis.append("FizzBuzz")
            elif div_3:
                lis.append("Fizz")
            elif div_5:
                lis.append("Buzz")
            else: lis.append(str(i))
        return lis
