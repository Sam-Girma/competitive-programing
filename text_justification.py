class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        curr_line = []
        curr_w_len = 0
        for w in words:
            if curr_w_len + (len(curr_line) - 1) + (len(w) + 1) > maxWidth:
                spaces = maxWidth - curr_w_len
                
                added = 0
                j = 0
                while added < spaces:
                    if j >= len(curr_line) - 1:
                        j = 0
                    
                    # print(j)
                    # print(curr_line)
                    curr_line[j] += " "
                    added += 1
                    j += 1
                
                res.append("".join(curr_line))
                curr_line = []
                curr_w_len = 0
            
            curr_line.append(w)
            curr_w_len += len(w)
        
        last_line = " ".join(curr_line)
        last_line += (" " * (maxWidth - len(last_line)))
        res.append(last_line)
        return res

		
