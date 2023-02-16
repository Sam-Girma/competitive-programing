class Solution:
    def getLengthOfOptimalCompression(self, s: str, K: int) -> int:
        n = len(s)
        
        @lru_cache(None)
        def search(i, k, prevC, prevN):
            if i < 0:
                return 0
            
            curC = s[i]
            res1 = res2 = 1000 
            if prevC == None:
                res1 = 1 + search(i-1, k, curC, 1)
            else:
                if prevC == curC:
                    res1 = (prevN in [1, 9, 99]) + search(i-1, k, curC, prevN + 1)
                else:
                    res1 = 1 + search(i-1, k, curC, 1)
                    
            if k > 0:
                res2 = search(i-1, k-1, prevC, prevN)
      
            return min(res1, res2)
        
        return search(n-1, K, None, None)
