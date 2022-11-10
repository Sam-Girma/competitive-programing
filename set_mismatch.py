class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        lost = duplicate = 0
        for i in range(1, len(nums)+1):
            if i not in count:
                lost = i
            elif count[i]==2:
                duplicate = i
            if lost and duplicate:
                return [duplicate, lost]
            

