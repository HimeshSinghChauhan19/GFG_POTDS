class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        
        ind1,ind2=None,None
        # Getting the first ind after leading zeros
        for i in range(len(s1)):
            if(s1[i]!='0'):
                ind1=i
                break
        for j in range(len(s2)):
            if(s2[j]!='0'):
                ind2=j
                break
        
        # Will get the necessary part of the strings and convert them to integers
        num1,num2=int(s1[ind1:]),int(s2[ind2:])
        return num1*num2