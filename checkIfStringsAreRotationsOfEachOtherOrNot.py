#User function Template for python3

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        n=len(s1)
        for i in range(n):
            
            it1=0
            if(s2[i]==s1[it1]):
                it2=i
                count=0
                done=True
                
                while(count<n):
                    if(s2[it2]!=s1[it1]):
                        done=False
                        break
                    it1+=1
                    it2=(it2+1)%n
                    count+=1
                if(done==True):
                    return 1
        return 0
        
        
        # FAILED TIME CONSTRAINTS
        # def rotateAC(st,n):
        #     ''' to rotate st anticlockwise by n places '''
        #     # normalizing n 
        #     n=n%len(st)
        #     for i in range(n):
        #         st=st[1:]+st[0]
        #     return st
            
        # def rotateC(st,n):
        #     ''' to rotate st clockwise by n places '''
        #     # normalizing n 
        #     n=n%len(st)
        #     for i in range(n):
        #         st=st[-1]+st[:-1]
        #     return st
            
        # for i in range(len(s1)):
        #     if(s1==rotateAC(s2,i)):
        #         return 1
        
        # return 0
