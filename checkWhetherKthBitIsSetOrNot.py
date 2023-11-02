class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        return False if(k>=len(bin(n))-2) else bin(n)[-k-1]=='1'