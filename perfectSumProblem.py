class Solution:
    
    def solve(self,arr,ind,currSum,sum,dp):
        
        if(ind>=len(arr)):
            return 0
            
        sc1=0
        if(dp[ind][currSum]!=-1):
            return dp[ind][currSum]
            
        if(currSum+arr[ind]==sum):
            sc1=1
            # Even when we have the summation currently, it is possible
            # that, we may have 0's at the right, so we gotta look at them too,
            
            
        if(currSum+arr[ind]<=sum):
            sc1+=self.solve(arr,ind+1,currSum+arr[ind],sum,dp)
            
        sc2=self.solve(arr,ind+1,currSum,sum,dp)
            
        dp[ind][currSum]=(sc1+sc2)%(1000000000+7);
        return dp[ind][currSum]
        
	def perfectSum(self, arr, n, sum):
		# code here
		dp=[[-1 for i in range(sum+1)] for j in range(n+1)]
        ans=self.solve(arr,0,0,sum,dp)
        return ans