import math
class Solution:
    def nCr(self, n, r):
        # code here
        if(r>n):
            return 0
        return ((math.factorial(n))//(math.factorial(n-r)*math.factorial(r)))%(pow(10,9)+7)