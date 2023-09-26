import heapq as HP

class Solution:
    def maxCombinations(self, n, k, A, B):
        # Code here
        A.sort()
        B.sort()
        ans=[]
       
        # the combinations that are considered, and won't consider them again
        done_combs=set()
        
        # To make this a heap and get the largest sums using heapq
        arr=[]
        # makes the arr a heap inplace, the heap structure will help us to 
        # get the largest sums easily
        HP.heapify(arr)
        
        ''' 
         basically for k times, will be considering all the possibilities,
         for example if we just considered ith elem from A, and jth elem from B
         1) then next will consider i-1th elem from A with jth elem from B
         2) and will consider ith elem from A with j-1th elem from B 
        '''
        
        # will store the sums alongwith the indices, so that later can consider the 
        # further cases,
        
        '''
         also, will be storing sums in their negative form, bcz heapq keeps the
         arr in ascending, order, 
         so to get the arr in the descending order, will store their negatives
         like instead of storing [1,2,3,4,5] will store [-1,-2,-3,-4,-5],
         so the heapq will give us 1 in the first type of array and -5 in the 2nd one
        '''
        HP.heappush(arr, ( -A[n-1]-B[n-1],(n-1,n-1) ) )
        done_combs.add((n-1,n-1))
       
        for _ in range(k):
            
            best=HP.heappop(arr)
            # best=(1,(1,1))
            # adding the summation to the ans array
            ans.append(0-best[0])
            # adding the indices so they are not repeated
            # done_combs.add(best[1])
            
            # print(best)
            
            i=best[1][0]
            j=best[1][1]
            
            # dp[i][j]=1
            # if(i==0 or j==0):
            #     return ans
            
            if((i-1,j) not in done_combs):
                done_combs.add((i-1,j))
                HP.heappush(arr,( -A[i-1]-B[j] ,(i-1,j)))
                
            if((i,j-1) not in done_combs):
                done_combs.add((i,j-1))
                HP.heappush(arr, ( -A[i]-B[j-1] ,(i,j-1) ) )
            # now just repeat this for k times, bcz everytime will get a max sum
            
        # print(ans)
        return ans