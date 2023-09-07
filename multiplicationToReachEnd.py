class Solution:
    
    def minimumMultiplications(self, arr, start, end):
        # code here
        if(start==end):
            return 0
            
        dp=[-1]*100000
        queue=[]
        
        dp[start]=0
        queue.append(start)
        
        while(len(queue)!=0):
            elem=queue[0]
            queue.pop(0)
            
            for i in range(len(arr)):
                mul=(elem*arr[i])%100000
                
                if(dp[mul]==-1):
                    queue.append(mul)
                    dp[mul]=dp[elem]+1    
                    
                    if(mul==end):
                        return dp[mul]
                        
        return -1