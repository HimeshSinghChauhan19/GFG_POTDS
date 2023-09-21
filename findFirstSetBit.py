class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        for ind,bit in enumerate(reversed(str(bin(n))[2:]),start=1):
            if(bit=='1'):
                return ind
        return 0