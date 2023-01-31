class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window_map = Counter(blocks[:k])
        left = 0
        right = k
        minim = window_map["W"]
        while(right<len(blocks)):
            window_map[blocks[left]]-=1
            window_map[blocks[right]]+=1
            minim = min(minim, window_map["W"])
            right+=1
            left+=1
        return minim
