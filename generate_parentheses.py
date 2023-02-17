class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        valid_one = []
        def backtrack(opened, closed):
            print(valid_one)
            if opened==closed==n:
                result.append("".join(valid_one))

            if opened<n:
                valid_one.append("(")
                backtrack(opened+1, closed)
                valid_one.pop()
            if closed<opened:
                valid_one.append(")")
                backtrack(opened, closed+1)
                valid_one.pop()
        backtrack(0, 0)
        return result
