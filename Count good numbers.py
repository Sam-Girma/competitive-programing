class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n%2==0:
            return (pow(5,n//2,pow(10,9)+7)*pow(4,n//2,pow(10,9)+7))%(pow(10,9)+7)
        else:
            return (pow(5,(n//2)+1,pow(10,9)+7)*pow(4,n//2,pow(10,9)+7))%(pow(10,9)+7)
        
