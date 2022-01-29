class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        count_no_of_piles=0
        while(len(piles)!=0):
            bob,you,alice=piles[0],piles[-2],piles[-1]
            count_no_of_piles+=piles[-2]
            piles.pop()
            piles.pop(0)
            piles.pop()
        return count_no_of_piles
            
        
