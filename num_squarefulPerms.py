class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        self.count = 0
        def backtrack(freq,path):
            
            if freq=={}:  
                self.count+=1
                return 
            for i in list(freq.keys()):
                if not path:
                    if freq[i]==1:
                        del freq[i]
                    else:
                        freq[i]-=1
                    backtrack(freq,path+[i])
                    freq[i]+=1
                else:
                    if freq[i]==1:
                        del freq[i]
                    else:
                        freq[i]-=1
                    if int((i+path[-1])**(0.5))==(i+path[-1])**(0.5):
                        backtrack(freq,path+[i])
                    freq[i]+=1
        
        backtrack(Counter(A),[])
        return self.count
