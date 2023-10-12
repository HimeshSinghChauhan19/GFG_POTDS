class Solution:
    def romanToDecimal(self, S): 
        # code here
        i=0
        vals={
           'I':1,
           'V':5,
           'X':10,
           'L':50,
           'C':100,
           'D':500,
           'M':1000
        }
        ans=0
        while(i<len(S)):
            
            # checking if the next char is of greater value than the curr one
            if((i+1)<len(S)):
                if(vals[S[i]]<vals[S[i+1]]):
                    # means these 2 chars are one whole value
                    # that is next_char_value-curr_char_value
                    ans+=(vals[S[i+1]]-vals[S[i]])
                    i+=2
                    continue
            ans+=vals[S[i]]
            i+=1
            
        return ans