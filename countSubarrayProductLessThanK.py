class Solution:
    def countSubArrayProductLessThanK(self, arr, n, k):
        
        # Using the Sliding Window Approach
        it1,it2=0,0
        ans=0
        prod=arr[0]
        
        while(it1<n and it2<n):
            
            # Checking the condition
            if(prod<k):
                # Add the length of the sliding window to the ans variable
                ans+=it2-it1+1
                it2+=1
                # whenever we go out of bound, then will not be accessing the arr anymore, so just get out of the loop
                if(it2==n):
                    break
                prod=prod*arr[it2]
            else:
                # remove the contribution of ith elem to the prod 
                # and then increase it1
                # Note that prod will be completely divided cause, it1'th elem was 
                # multiplied to prod before, 
                ''' Handling a case: like n=4,k=1,arr=[2,2,2,2], so increase both it1 and it2 and update the prod, ignoring the values left behind,
                 bcz they are of no use ''' 
                if(it1==it2):
                    it1+=1
                    it2+=1
                    # Also check if we have reached the end of the array, then we can't update the prod to index it1, bcz it1 can be equal to n-1
                    if(it1>=n):
                        break
                    # Else just update the prod and go for the next iteration by the continue keyword
                    prod=arr[it1]
                    continue
                while(prod>=k and it1<=it2):
                    prod=prod//arr[it1]
                    it1+=1
        return ans