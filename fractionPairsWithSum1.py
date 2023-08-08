class Solution:
    def countFractions(self, n, numerator, denominator):
        # Your code here
        # 0.333,0.1,3.858,0.9,0.4
        
        # Sorted:-
        # 1/10 , 3/9   , 2/5  , 12/18 , 81/90  
        # 0.1  , 0.333 , 0.4  , 0.666 , 0.9 
        i,j=0,n-1
        count=0
        
        data=[ numerator[i]/denominator[i] for i in range(n) ]
        
        
        data.sort()
        # print(data)
        while(i<j):
            if(data[i]+data[j]<1):
                i+=1
            elif(data[i]+data[j]>1):
                j-=1
            else:
                # print(data[i],data[j])
                # Just considering all the vals that satisfy the condition with the
                # ith value, and then when are done with this ith val then just 
                # incrementing the value of i, to consider new fresh cases
                prev_j_val=j
                
                while(data[i]+data[j]==1 and i<j):
                    count+=1
                    j-=1
                    
                j=prev_j_val
                i+=1
                
                # The below code is logically incorrect for test cases like: 
                # 0.1,0.1,0.9,0.9,0.9
                # basically in such cases the below logic will consider first 0.1, 
                # with all the 0.9s but the second 0.1, will be only considered alongwith
                # the first 0.9, which will give wrong output eventually
                
                # count+=1
                # if(data[i]+data[j-1]>=1):
                #     j-=1
                # else:
                #     i+=1
        return count