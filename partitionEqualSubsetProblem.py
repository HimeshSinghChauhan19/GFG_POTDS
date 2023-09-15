import math
class Solution:
    def solve(self,arr,n,summation,ind,currSum,dp):
        ''' I just need the sum of any subsequence of nums to be summation '''
        if(ind>=n or currSum>summation):
            return 0
        
        if(currSum+arr[ind]==summation):
            return 1
        
        if(dp[ind][currSum]!=-1):
            return dp[ind][currSum]
            
        # simple, for each elem either take it or ignore it
        # and give the best result possible over the 2 cases
        
        '''
        the below line is a very tricky logical error, bcz we are calculating
        the whole problem and then storing the result which is of no use at all
        -Took some minutes to get this concept.
        '''
        # dp[ind][currSum]=max(self.solve(arr,n,summation,ind+1,currSum+arr[ind],dp),self.solve(arr,n,summation,ind+1,currSum,dp))
        
        choice1=self.solve(arr,n,summation,ind+1,currSum+arr[ind],dp)
        if(choice1==1):
            dp[ind][currSum]=choice1
            return choice1
            
        choice2=self.solve(arr,n,summation,ind+1,currSum,dp)
        dp[ind][currSum]=max(choice1,choice2)
        return dp[ind][currSum]
        
    def equalPartition(self, N, arr):
        # code here
        summation=sum(arr)/2
        # bcz the two halves after parition need to have the same summation
        # that is possible only when the sum can be divided into parts, so 
        # i can check that prior only
        ''' Checking if the summation is a an integer and not a decimal '''
        if(math.floor(summation)!=math.ceil(summation)):
            return 0
            
        # dp to store the intermediate results
        dp=[[-1 for i in range(int(summation)+1)] for j in range(N+1)]
        # print("There will be some ans to this")
        ans=self.solve(arr,N,summation,0,0,dp)
        return ans