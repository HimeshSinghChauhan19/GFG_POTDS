class Solution:
    def klengthpref(self,arr,n,k,s):
        # return list of words(str) found in the board
        prefix=s[:k]
        count=0
        
        if(k>len(s)):
            return 0
        for st in arr:
            if(st[:k]==prefix):
                count+=1
        return count