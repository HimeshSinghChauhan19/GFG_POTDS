class Solution:
    #Complete this function
    def power(self,N,R):
        pass
        # the built-in function is expected to provide O(log n) TC, but fails
        # return pow(N,R)
        
        # Failed! Just 10 cases passed, although this gives, O(n) I knew but the 
        # below implementations were giving O(logn) but still they were
        # failing, so just wanted to check in case...
        # ans=1
        # for i in range(y):
        #     ans*=x
        # return ans
        
        # Failed, Same, tried this same appraoch and it passed all the test cases in 
        # C++, ;( 
        # temp = 0
        # if(y == 0):
        #     return 1
        # temp = self.power(x, int(y / 2))
        # res = temp*temp
        # if (y % 2 == 0):
        #     return res
        # else:
        #     return x * res
        
        # Failed, same again
        # return N**R % 1000000007
        
        # Failed, 
        # return round(math.exp(math.log(N)*R)) % 1000000007