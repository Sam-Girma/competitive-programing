class Solution:

    def __init__(self, w: List[int]):
        self.summ = [0]
        for i in range(len(w)):
            self.summ.append(self.summ[-1]+w[i])

    def pickIndex(self) -> int:
        val = random.randint(1, self.summ[-1])
        idx = 0
        for i, v in enumerate(self.summ):
            if v >= val:
                idx = i -1
                break
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
