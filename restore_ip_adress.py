class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        possible_ip = []
    
        def backtrack(idx, curr):
            print(curr)
            if idx>=len(s):
                if len(curr)==4:
                    ip = "".join(curr)[:-1]
                    if ip not in possible_ip:
                        possible_ip.append("".join(curr)[:-1])
                return
            if s[idx] == "0":
                curr.append("0.")
                backtrack(idx+1, curr)
                curr.pop()
            else:
                curr.append(s[idx]+".")
                backtrack(idx+1, curr)
                curr.pop()
                curr.append(s[idx:idx+2]+".")
                backtrack(idx+2, curr)
                curr.pop()
                if int(s[idx])<=2:
                    if not(idx+2<len(s) and int(s[idx:idx+3])>255):
                        curr.append(s[idx:idx+3]+".")
                        backtrack(idx+3, curr)
                        curr.pop()
        backtrack(0, [])
        return possible_ip
                
