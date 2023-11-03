class Solution:

	def checkTriplet(self,arr, n):
    	# code here
        dic={i*i:i for i in arr}
        for i in dic:
            # here there is no requirement to check for i and j being elems at different indices
            # cause no 2 same elems will be satisfying the if condition, bcz the summation is never
            # gonna be a square of any number, like 4+4,9+9,16+16, etc.
            for j in dic:
                if((i+j) in dic):
                    return True
        return False