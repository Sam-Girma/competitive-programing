class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op=["*","+","/","-"]
        
        for i in range(len(tokens)):
            if (tokens[i] not in op):
                stack.append(int(tokens[i]))
                continue
            
            if tokens[i]=="*":
                stack.append(stack.pop()*stack.pop())
            elif tokens[i]=="+":
                stack.append(stack.pop()+stack.pop())
                
            elif tokens[i]=="-":
                stack.append(-(stack.pop()-stack.pop()))
            else:
                if stack[-2]==0:
                    stack.append(0)
                else:
                    stack.append(int(1/(stack.pop()/stack.pop())))
         
        return stack.pop()
        
