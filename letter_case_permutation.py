class Solution:
    def isAlpha(self, char):
        if "a"<=char<="z" or "A"<=char<="Z":
            return True
        return False
    def letterCasePermutation(self, s: str) -> List[str]:
        self.alpha_ind = []
        self.array_s = []
        for i in range(len(s)):
            self.array_s.append(s[i])
            if self.isAlpha(s[i]):
                self.alpha_ind.append(i)
        if len(self.alpha_ind)==0:
            return [s]

        self.permutations = []
        self.backtrack(0)
        return self.permutations
    
    def backtrack(self, index):
        if index==len(self.alpha_ind)-1:
            self.array_s[self.alpha_ind[index]]=self.array_s[self.alpha_ind[index]].lower()
            self.permutations.append("".join(self.array_s))
            self.array_s[self.alpha_ind[index]] = self.array_s[self.alpha_ind[index]].upper()
            self.permutations.append("".join(self.array_s))
        else:
            self.array_s[self.alpha_ind[index]] = self.array_s[self.alpha_ind[index]].lower()
            self.backtrack(index+1)
            self.array_s[self.alpha_ind[index]] = self.array_s[self.alpha_ind[index]].upper()
            self.backtrack(index+1)
        
        

           

           
