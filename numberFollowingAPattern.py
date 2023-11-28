#User function Template for python3
class Solution:
    def printMinNumberForPattern(self,S):
        # will track the max number used till any pt. of time
        curr_max=1
        # will be used when will get D's, cause we need to store curr_max, so curr_num will only be updated in case of a D
        curr_num=1
        
        # dp[i] will contain the no. of consecutive D's after i'th position
        dp=[0 for i in range(len(S))]
        d_count=0
        
        # handling D's at the starting of the string
        start_d_count=0
        for i in range(len(S)):
            if(S[i]=='D'):
                start_d_count+=1
            else:
                break
            
        # simply, the curr_max will start from (the d_count in the starting)+1
        curr_max=start_d_count+1
        curr_num=curr_max
        
        ans=str(curr_max)
        
        
        for i in range(len(S)-1,-1,-1):
            
            if(S[i]=='D'):
                d_count+=1
            elif(d_count!=0):
                dp[i]=d_count
                d_count=0
                
                
        for i in range(len(S)):
            
            if(S[i]=='I'):
                
                if(dp[i]!=0):
                    # dp[i] will contain the no. of D's after this I
                    curr_max=curr_max+dp[i]+1
                    ans+=str(curr_max)
                    curr_num=curr_max
                    continue
                
                # if there are no D's after this I, then just inc. the curr_max and append to ans
                ans+=str(curr_max+1)
                curr_max+=1
            
            if(S[i]=='D'):
            
                # for a D, will just decr. the curr_num and append to ans
                curr_num-=1
                ans+=str(curr_num)    
                
        return ans