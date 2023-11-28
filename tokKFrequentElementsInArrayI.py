from collections import Counter as CT
class Solution:
    
    def topK(self, nums, k):
        
        ans=list()
        # the freqs will be indices and the elems having that freq will be a part of that index
        freqs=[[] for i in range(len(nums)+1)]
        
        # the elems with their respective frequencies, a list of tuples
        ls=sorted(dict(CT(nums)).items(),key=lambda x:x[1],reverse=True)
        
        # going through ls to group the elems with same freq together
        for i,j in ls:
            freqs[j].append(i)
            
        # the elems with same freq will be sorted in decreasing order, that's it
        for i in range(len(freqs)-1,-1,-1):
            ans+=sorted(freqs[i],reverse=True)
       
        # will take only the first k elems from the answer
        return ans[:k]
        