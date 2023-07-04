class Solution:
    def isDivisible(self, s):
        # code here
        # Will just convert this string to decimal number using the int function
        s=int(s,base=2)
        return 1 if(s%3==0) else 0