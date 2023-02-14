class Solution:
    def minimumDeletions(self, s):
        delete, count = 0, 0
        for i in s:
            if i == 'b':
                count += 1
            elif count:
                delete += 1
                count -= 1
        return delete
