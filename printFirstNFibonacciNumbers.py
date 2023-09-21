class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        ans=[]
        a,b,c=1,1,0
        for i in range(n):
            ans.append(a)

            c=a+b
            a=b
            b=c
        return ans