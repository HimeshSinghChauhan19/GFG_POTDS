class Solution:
    def is_bleak(self, n):
        # Code here
        def count_set_bit(num):
            ans=0
            while(num>0):
                ans+=(num & 1)
                num=num>>1
            return ans;
        
        '''
        bcz we need the summation to be n, so if we think about it
        then we can have atmost 30 setbits in a number, cause
        boundation is 10^9, so the rest part needs to be fulfilled
        by the positive integer and thus we just have to check 
        for the numbers which are 30 behind this n
        '''
        # and thus the Time Complexity reduces to O(log^2(n))
        for i in range(n-30,n+1):
            if i + count_set_bit(i)==n:
                return 0
        return 1