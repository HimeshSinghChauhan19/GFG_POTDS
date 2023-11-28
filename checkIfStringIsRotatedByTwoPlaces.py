#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        def rotateAC(st,n):
            ''' to rotate st anticlockwise by n places '''
            # normalizing n 
            n=n%len(st)
            for i in range(n):
                st=st[1:]+st[0]
            return st
            
        def rotateC(st,n):
            ''' to rotate st clockwise by n places '''
            # normalizing n 
            n=n%len(st)
            for i in range(n):
                st=st[-1]+st[:-1]
            return st
            
        # print(rotateAC('amazon',2))
        # print(rotateC('amazon',2))
        
        return rotateAC(str1,2)==str2 or rotateC(str1,2)==str2