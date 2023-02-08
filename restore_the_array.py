class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs = defaultdict(list)
        starts = set()
        for pair in adjacentPairs:
            if pair[0] in starts: starts.remove(pair[0])
            else: starts.add(pair[0])
            if pair[1] in starts: starts.remove(pair[1])
            else: starts.add(pair[1])
            pairs[pair[0]].append(pair[1])
            pairs[pair[1]].append(pair[0])
        nums= []
        for i in starts:
            nums.append(i)
            break
        visited = set(nums)
        for i in range(len(adjacentPairs)):
            for ele in pairs[nums[-1]]:
                if ele not in visited:
                    nums.append(ele)
                visited.add(ele)
        return nums
