class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        self.s.append(x)
        
    def pop(self):
        #CODE HERE
        return self.s.pop() if(len(self.s)>=1) else -1

    def getMin(self):
        #CODE HERE
        return min(self.s) if(len(self.s)>=1) else -1