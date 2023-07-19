class Solution:
    
    def subSeqPalinsLen(self,string,l,r,dp):
        ''' Simple Recursive Approach with Memoization '''
        if(dp[l][r]!=-1):
            return dp[l][r]
            
        if(l==r):
            dp[l][r]=1
            return 1
        if(l>r):
            dp[l][r]=0
            return 0
        
        if(string[l]==string[r]):
            # Means we can explore this further, there is a chance for a good sized
            # palindrome here
            # also, this means that there is atleast a 2 sized palin here
            dp[l][r]=2+self.subSeqPalinsLen(string,l+1,r-1,dp)
            return dp[l][r]
        # when the elems are not the same,
        dp[l][r]=max(self.subSeqPalinsLen(string,l+1,r,dp),self.subSeqPalinsLen(string, l,r-1,dp))
        return dp[l][r]
    
    def longestPalinSubseq(self, S):
        ''' Just uses the helper function to get the result '''
        dp=[[-1 for i in range(len(S))] for j in range(len(S))]
        
        return self.subSeqPalinsLen(S,0,len(S)-1,dp) 