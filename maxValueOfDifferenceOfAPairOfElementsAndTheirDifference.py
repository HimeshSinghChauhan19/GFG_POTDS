class Solution:
    def maxValue(self, arr, N):
        # code here 
        max_sum=0
        arr=list(zip(arr,[i for i in range(N)]))
        arr.sort(key=lambda x:x[0])
        for i in range(N-1,0,-1):
            max_sum=max(max_sum,abs(arr[0][0]-arr[i][0])+abs(arr[i][1]-arr[0][1]))
            
        # for i in range(N-1):
        #     for j in range(i+1,N):
        #         max_sum=max(max_sum,abs(arr[i]-arr[j])+abs(i-j))

        return max_sum