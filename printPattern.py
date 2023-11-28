import sys
sys.setrecursionlimit(10**6)
class Solution:
    def solve(self,arr,n):
        if(n<=0):
            arr.append(n)
            return arr
        arr.append(n)
        arr=self.solve(arr,n-5)
        arr.append(n)
        return arr
        
    def pattern(self, N):
        # code here
        ans=list()
        ans=self.solve(ans,N)
        return ans