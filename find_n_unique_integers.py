class Solution:
    def sumZero(self, n: int) -> List[int]:
        retarray = []
        for i in range(1, n//2+1):
            retarray.append(i)
            retarray.append(-i)
        if n%2:
            retarray.append(0)
        return retarray
