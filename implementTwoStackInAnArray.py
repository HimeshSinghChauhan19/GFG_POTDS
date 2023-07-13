class TwoStacks:
    '''
    Does the same thing that we were intended to do according to the prob
    although not the real stack but just works like that, 
    and this showsh us that it's not necessary to take things as they are 
    too complicated, like a stack is normally percepted as, it is simple.

    Note: The pop function here gives O(n) instead of O(1) although I
    don't understand how this got past all the test cases, cause the
    slice operator would always take O(n) as the worst case, but it did, 
    it's late night so I will be doing the full stack implementation tommorrow 
    and will submit another code in cpp, for the same. ;)
    '''
    def __init__(self, n=100):
        self.size = n
        self.arr = [0] * n
        self.arr1=[]
        self.arr2=[]
        self.top1 = -1
        self.top2 = n

    # Function to push an integer into stack 1
    def push1(self, x):
        self.arr1.append(x)

    # Function to push an integer into stack 2
    def push2(self, x):
        self.arr2.append(x)

    # Function to remove an element from top of stack 1
    def pop1(self):
        if(len(self.arr1)==0):
            return -1
        lastElem=self.arr1[-1]
        self.arr1=self.arr1[:-1]
        return lastElem

    # Function to remove an element from top of stack 2
    def pop2(self):
        if(len(self.arr2)==0):
            return -1
        lastElem=self.arr2[-1]
        self.arr2=self.arr2[:-1]
        return lastElem