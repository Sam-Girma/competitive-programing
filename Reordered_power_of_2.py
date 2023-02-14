class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = set()
        for i in range(30):
            number = "".join(sorted(str(pow(2, i))))
            powers.add(number)
        print(powers)
        return "".join(sorted(str(n))) in powers
