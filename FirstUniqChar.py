class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictt = Counter(s)
        for i in range(len(s)):
            if dictt[s[i]]==1:
                return i
        return -1
