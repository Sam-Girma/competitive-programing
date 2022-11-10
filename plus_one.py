class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        index = len(digits)-1
        while(index>=0 and add):
            add = (digits[index]+1)//10
            digits[index] = (digits[index]+1)%10
            index-=1
        if add:
            return [1]+digits
        return digits
            
