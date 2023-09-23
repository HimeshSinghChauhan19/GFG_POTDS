class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	# bcz the values in the array are going to be maximum n-1, so 
    	# will be using Count Sort technique to get the frequency too and also
    	# the order will be maintained in that way
    	
    	ans=[-1]
    	dp=[0]*(max(arr)+1)
    	
    	for i in range(n):
    	    dp[arr[i]]+=1
        
        for i in range(max(arr)+1):
            if(dp[i]>1):
                # when the freq of this elem(that is the index) is >1
                # means we gotta put this to ans
                ans.append(i)
                
        # if there won't be any duplicate elems in the arr, then just return -1
        # Remember if it's just -1 in the ans array(means len 1) then, we just return 
        # ans, but otherwise, when we have atleast one other elem, then we need to 
        # ignore the -1 in the ans array
        return ans if(len(ans)==1) else ans[1:]