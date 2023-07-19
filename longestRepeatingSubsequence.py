class Solution:
    def solve(self,i,j,st1,st2,dp):
        if(i<0 or j<0):
            return 0
        if(dp[i][j]!=-1):
            return dp[i][j]
        
        # If the condition is satisfied then we can look further for this 
        if(st1[i]==st2[j] and i!=j):
            dp[i][j]=1+self.solve(i-1,j-1,st1,st2,dp)
            return dp[i][j]
            
        dp[i][j]=max(self.solve(i-1,j,st1,st2,dp),self.solve(i,j-1,st1,st2,dp))

        return dp[i][j]
        
    def LongestRepeatingSubsequence(self, str):
        st2="".join(list(str).copy())
        dp=[[-1 for i in range(len(str))] for j in range(len(str))]
        return self.solve(len(str)-1,len(str)-1,str,st2,dp)