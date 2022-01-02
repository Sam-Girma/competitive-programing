class MyQueue:

    def __init__(self):
        self.lst = []
        self.qlst = []
        

    def push(self, x: int) -> None:
        self.lst.append(x)
        
 
    def pop(self) -> int:
        for i in range(len(self.lst)):
            self.qlst.append(self.lst.pop())
        a=self.qlst.pop()
        for i in range (len(self.qlst)):
            self.lst.append(self.qlst.pop())
        return a
        
        

    def peek(self) -> int:
        for i in range(len(self.lst)):
            self.qlst.append(self.lst.pop())
        a=self.qlst[-1]
        for i in range (len(self.qlst)):
            self.lst.append(self.qlst.pop())
        return a
        
        

    def empty(self) -> bool:
        return len(self.lst)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
