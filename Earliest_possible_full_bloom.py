class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        def cmp(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            return b[1] - a[1]
        arr = []
        for i in range(len(plantTime)):
            arr += [[growTime[i] + 1, plantTime[i]]]
        arr.sort(key=cmp_to_key(cmp))
        ans = 0
        print(arr)
        for i in arr:
            print(i)
            ans = max(ans, i[0])
            ans += i[1]
            print(ans)
        return ans - 1
