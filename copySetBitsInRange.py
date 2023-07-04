class Solution:
    def setSetBit(self, x, y, l, r):
        # will just get the part of the y that needs to be set in x, 
        y=bin(y)[2:]
        y=list(reversed(y))
        '''
         again a reversed operation, then converting to a string again 
         worst case should be O(30) that is constant, convert it to int and then
         fill the right space with zeros, so we get the number that we wanna
         OR the int x with, the number of zeros in the right will be l-1
        '''
        # range_part="".join(reversed(y[l-1:r]))
        
        # had to handle this case, bcz
        '''
        Suppose l==r and also they are l,r>len(y),
        means here the range_part will have nothing inside it, so 
        will have an empty list and then an empty string, which will eventually 
        result in an error inside the int() contructor
        
        UPDATE:
        Considered the above problem and gave a condition inside the int constructor
        instead of making a variable range_part and having the below condition.
        '''
        # if(len(range_part)==0):
        #     return x
        return int("".join(reversed(y[l-1:r])) if(len(y[l-1:r])!=0) else '0',base=2)<<(l-1)|x
    