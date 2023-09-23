class Solution:  
    
    # def solve(self,a,n,ind,dp):
    #     if(ind>=n):
    #         return 0
        
    #     if(dp[ind]!=-1):
    #         return dp[ind]
            
    #     if(ind==n-1):
    #         # if we get to the last elem, then this is the best we got
    #         # means, if we ignore this(which will be giving 0) or we take this(a[n-1])
    #         return a[n-1]
        
    #     # either take this elem(then gotta skip the next elem and go to ind+2'th elem, 
    #     # or just ignore it and go to the next one, for choosing again
    #     choice1=a[ind]+self.solve(a,n,ind+2,dp)
    #     choice2=self.solve(a,n,ind+1,dp)
        
    #     dp[ind]= max(choice1,choice2)
    #     return dp[ind]
        
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        # using the tabulation approach
        dp=[0]*n
        dp[0]=a[0]
        
        for i in range(1,n):
            choice1=a[i]
            choice2=dp[i-1]
            # if we have an elem 2 places behind, then we can have that wil a[i] too
            # cause that's not consecutive with i'th element
            if(i-2>=0):
                # this means the best answer of i-2 pos. elem. combined with i'th elem
                choice1+=dp[i-2]
            
            # the result for this i'th position will be the best choice b/w these 2
            dp[i]=max(choice1,choice2)
            
        return dp[n-1]
        
        ''' could have used the Recursion + DP approach too '''
        # for some unknown reason this methods is giving seg fault in 1110 TC
        # that makes no sense because seg fault doesn't just happend like that in 
        # just 1 case, all boundations are fine and also there is no corner case
        
        # dp=[-1]*n
        # ans=self.solve(a,n,0,dp)
        # return ans
