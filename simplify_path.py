class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""
        
        for letter in path:
            if letter == "/":
                if curr == "" or curr == ".":
                    curr = ""
                elif curr == "..":
                    if stack:
                        stack.pop()
                    curr = ""
                else:
                    stack.append(curr+"/")
                    curr = ""
            else:
                curr += letter
                
        if curr == "" or curr == ".":
                    curr = ""
        elif curr == "..":
            if stack:
                stack.pop()
        else:
            stack.append(curr+"/")
            
        return "/"+"".join(stack)[:-1]
