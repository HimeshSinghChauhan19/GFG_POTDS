class Solution:
    def sumOfDivisors(self, N):
    	#code here 
        ans=0
        for i in range(1,N+1):
            # print(N//i)
            ans+=i*(N//i)
        return ans