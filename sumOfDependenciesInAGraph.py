class Solution:
    def sumOfDependencies(self,adj,V):
        #code here
        # Little bit of Python Magic
        return sum(list(map(lambda x:len(x),adj)))
        