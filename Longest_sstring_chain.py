class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        max_length = 0
        word_set = set(words)
        words.sort(key=lambda x: len(x))
        
        @lru_cache
        def dp(word):
            cur_max_length = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]
                if new_word in word_set:
                    cur_max_length = max(cur_max_length, 1 + dp(new_word))
            
            return cur_max_length
        
        for word in words:
            max_length = max(max_length, dp(word))
            
        return max_length
