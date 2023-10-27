class Solution:
    def func(self,st,i,j,dp):
        if(i>j):
            return 0
        choice1,choice2=0,0
        
        if(dp[i][j]!=-1):
            return dp[i][j]
            
        if(st[i]==st[j]):
            if(i==j):
                dp[i][j]=1
                return 1
            else:
                dp[i][j]=2+self.func(st,i+1,j-1,dp)
                return dp[i][j]
        else:
            choice1=self.func(st,i+1,j,dp)
            choice2=self.func(st,i,j-1,dp)
            dp[i][j]= max(choice1,choice2)
            
            return dp[i][j]
            
    def minimumNumberOfDeletions(self,S):
        # code here 
        dp=[[-1 for i in range(len(S))] for j in range(len(S))]
        mx_size=self.func(S,0,len(S)-1,dp)
        return len(S)-mx_size
