class Solution:
	def distinctSubsequences(self, S):
		# code here
		n=len(S)
		
        sub_counts=[0 if(i==0) else 1 for i in range(n+1)]
        sub_counts[0]=1
        last_occuring_indices={}
        
        for i in range(1,n+1):
            ch=S[i-1]
            if(ch in last_occuring_indices):
                last_ind = last_occuring_indices[ch]
                last_sub_count = sub_counts[last_ind]
                
                sub_counts[i]=((sub_counts[i-1]*2)-last_sub_count)%(1000000000+7)
                last_occuring_indices[ch]=i-1
                continue
            last_occuring_indices[ch]=i-1
            sub_counts[i]=sub_counts[i-1]*2
            
        return sub_counts[n]