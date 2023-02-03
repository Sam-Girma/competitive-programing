class Solution:
    def validPalindrome(self, s: str) -> bool:
        @cache
        def checker(left, right, trial):
            if left>=right:
                return True
            if s[left] == s[right]:
                return checker(left+1, right-1, trial)
            else:
                if trial>0:
                    return False
                return checker(left+1, right, 1) or checker(left, right-1, 1)
        return checker(0, len(s)-1, 0)
        
