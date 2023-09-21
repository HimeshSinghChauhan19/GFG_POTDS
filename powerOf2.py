
class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        # print(str(bin(n))[-1])
        # print(str(bin(n)).count('1'))
        return True if(str(bin(n)).count('1')==1) else False