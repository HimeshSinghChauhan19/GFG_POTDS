class Solution:
    def columnWithMaxZeros(self,arr,N):
        # code here
        ans=-1
        mx_freq=0
        for i in range(N):
            freq=0
            for j in range(N):
                if(arr[j][i]==0):
                    freq+=1
            if(freq>mx_freq):
                mx_freq=freq
                ans=i
        
        return ans
        