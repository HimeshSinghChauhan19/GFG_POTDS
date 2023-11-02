class Solution:
    def sumXOR (self, arr, n) : 
        
        ans=0
        get_bit=1
        curr_bit_val=1
        for i in range(32):
            ones,zeros=0,0
            # getting the stats of this bit in all numbers
            for i in arr:
                if((i&get_bit)==0):
                    zeros+=1
                else:
                    ones+=1
                    
            # the total contribution of this bit
            total=ones*zeros
            
            # total bits contributed multiplied by the value of this bit
            ans+=total*curr_bit_val
            
            # updating the value of curr bit 
            curr_bit_val*=2
            
            # also updation in the value of get_bit
            get_bit<<=1     
                
        return ans    