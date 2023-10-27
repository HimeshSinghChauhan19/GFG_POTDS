import math
class Solution:
    def numberOfPaths(self, rows, columns):
        # Initialize the number of paths to 1
        # num_paths = 1
        
        # # Define a constant for modulo operation
        MOD = 10**9 + 7
        
        # # Calculate the number of paths using Combinatorics
        # for i in range(rows - 1):
        #     # Use Combinatorics to calculate C(i + n, i)
        #     num_paths = (num_paths * (i + columns)) % MOD 
            
        #     # Use the modular inverse to calculate C(i + 1, i)
        #     temp = pow(i + 1, MOD - 2, MOD)
            
        #     num_paths = (num_paths * temp) % MOD
        
        # return num_paths
        
        num = den = 1
        n=rows+columns-2
        p=MOD
        r=rows-1
        for i in range(r):
            num = (num * (n - i)) % p
            den = (den * (i + 1)) % p
        return (num * pow(den, p - 2, p)) % p
        # return int(num/den)%p
        
        # this below line is fine, but not optimal for time complexity, 
        # thus we use Modular Inverse method to calculate nCr, that's it 
        # return int(math.factorial(rows+columns-2)/(math.factorial(rows-1)*math.factorial(columns-1)))