class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        time =0
        while("01" in s):
            s = s.replace("01", "10")
            time+=1
        return time
