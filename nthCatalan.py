class Solution:
    
    def getAnswer(self,n,dp):
        ''' Uses Recursion with Memoization(using a 1D array of size n+1) '''
        # if(n<=1):
        #     return 1
        # if(n==2):
        #     return 2
        
        if(dp[n]!=-1):
            return dp[n]
            
        result=0
        for i in range(n):
            result+=self.getAnswer(i,dp)*self.getAnswer(n-i-1,dp)
        
        dp[n]=result
        return result
        
    def __init__(self):
        self.dp=[0]*(n+1)
        self.dp[0]=1
        self.dp[1]=1
        
    def findCatalan(self, n : int) -> int:
        # print(self.dp)
        # code here
        ''' Formula Based Approach '''
        # print(1e9+7)
        ans=factorial(2*n)//(factorial(n)*factorial(n+1))
        # if instead of below number would divide by 1e9+7, then gives logical error, although the
        # values are the same, still...
        return int(ans%(1000000007))
        
        ''' Recursion- would take a lot of time, so won't even try '''
        # if(n<=1):
        #     return 1
        # if(n==2):
        #     return 2
        
        # result=0
        # for i in range(n):
        #     result+=self.findCatalan(i)*self.findCatalan(n-i-1)
        
        # return result
        
        ''' Recursion + Memoization '''
        # dp=[-1]*(n+1)
        # dp[0]=1
        # dp[1]=1
        # dp[2]=2
        
        # this below type of e usage was giving a weird logical error for n=175
        # # return int(self.getAnswer(n,dp)%(1e9+7))
        
        # return int(self.getAnswer(n,dp)%(1000000007))
        
        
        
        
        # if(n<=1):
        #     return 1
            
        # if(self.dp[n]!=0):
        #     return self.dp[n]
        
        # for i in range(2,n+1):
        #     for j in range(i):
        #         self.dp[i]+=self.findCatalan(j)*self.findCatalan(i-j-1)
        
        
        # return round(self.dp[n]%(1000000007))

