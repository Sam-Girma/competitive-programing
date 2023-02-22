class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = {}
        already_mapped = set()

        for i in range(len(s)):
            if s[i] in mapper:
                if mapper[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in already_mapped:
                    mapper[s[i]] = t[i]
                    already_mapped.add(t[i])
                else:
                    return False
        
        return True
