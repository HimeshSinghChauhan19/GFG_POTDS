from math import log2,floor,ceil
class Solution:
    def setBits(self, N):
        # Defining an inner function
        def getCount(num):
            count=0
                # Can replace all the lines with this one line, 
                # both approaches give the same time complexity, that is O(log N)
            return bin(num)[2:].count('1')
        
        # This below approach is more conceptually clear and should be
        # understood first before going for binary string shortcut
        
        # if(floor(log2(num))==ceil(log2(num))):
        #     # print("Power!")
        #     return 1
        # # print("Before:",num)
        # while(num!=0):
        #     # Increase the count only when the rightmost bit is set to 1, else not
        #     if(num&1==1):
        #         count+=1
        #     else:
        #         pass
        #     num>>=1
        #     # print(f"Now: {num}")
        # return count
        return getCount(N)