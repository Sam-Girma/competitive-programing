class RecentCounter(object):

    def __init__(self):
        self.counter=0
        self.timequeue=[]
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.counter=0
        self.timequeue.append(t)
        self.timequeue.reverse()
        for i in self.timequeue:
            if i>=t-3000:
                self.counter+=1
            else:
                break
        self.timequeue.reverse()
        return self.counter
            
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
