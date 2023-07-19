from collections import OrderedDict as OD
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        dict1=OD()
        for i in range(len(s)):
            try:
                temp=dict1[s[i]]
                dict1[s[i]]=-1
            except Exception as e:
                dict1[s[i]]=1
                
        for char,freq in dict1.items():
            if(freq==1):
                return char
                
        return "$"