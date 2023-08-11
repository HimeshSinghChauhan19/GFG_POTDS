class Solution:
    # def largestPrimeFactor (self, N):
    #     # code here
    #     def isPrime(num):
    #         import math
    #         ''' Will just return whether the number is Prime or Not '''
    #         if(num<=1):
    #             return False
    #         if(num==2 or num==3):
    #             return True
    #         if(num%2==0 or num%3==0):
    #             return False
            
    #         # So till here I have checked the nums till 4, now will check for further
    #         # 6 increment, bcz the prime numbers can be represented in the form of 
    #         # 6n+1 or 6n-1
    #         for i in range(5,int(math.sqrt(num))+,6):
    #             if(num%i==0 or num%(i+2)==0):
    #                 return False
    #         return True
    #     for i in range(N,1,-1):
    #         if(N%i==0 and isPrime(i)):
    #             return i
    #     # When no answer exists, although will never be the case...
    #     return -1
    def largestPrimeFactor (self, n):
        if n <= 1:
            return n 
        
        largest_prime = -1
        
        while n % 2 == 0:
            largest_prime = 2
            n //= 2
        
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                largest_prime = i
                n //= i
        
        if n > 2:
            largest_prime = n
        
        return largest_prime