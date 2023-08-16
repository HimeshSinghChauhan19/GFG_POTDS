from collections import Counter as CT
class Solution:
	def singleNumber(self, nums):
	    ''' 
	    A normal approach 
	    '''
		'''
		ans=list()
		freqs=dict(CT(nums))
 		for val,freq in freqs.items():
		    ans.append(val) if(freq==1) else None
		ans.sort()
		return ans
		'''
		
		'''
		A single liner to do the works of the above ways
		'''
		return sorted(list(filter(lambda x:x!=-1,[val if(freq==1) else -1 for val,freq in dict(CT(nums)).items()])))
		