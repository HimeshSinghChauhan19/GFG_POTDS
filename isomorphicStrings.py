#User function Template for python3
from collections import Counter as CT
class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        dt=dict()
        # if len not same, then can't do anything
        if(len(str1)!=len(str2)):
            return 0
            
        for i in range(len(str1)):
            dt[str1[i]]=dt.get(str1[i],'buzz')
            prev_mapping=dt[str1[i]]
            # if this is not the first instance of this char in str1 and the char it is mapped to, is not the curr str2 char, 
            # then means, we got 2 chars for a char in str1
            if(prev_mapping!='buzz' and prev_mapping!=str2[i]):
                return 0
            else:
                dt[str1[i]]=str2[i]
                
        # if there is any char in str2 to which 2 or more chars in str1 are mapped, then return 0
        freqs=dict(CT(dt.values())).values()
        for freq in freqs:
            if(freq!=1):
                return 0
        
        return 1
        