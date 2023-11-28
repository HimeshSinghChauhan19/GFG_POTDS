class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here 
        upper_sum=0
        it=0
        for i in range(n):
            for j in range(it,n):
                upper_sum+=matrix[i][j]
            it+=1
        lower_sum=0
        
        it=1
        for i in range(n):
            for j in range(0,it):
                lower_sum+=matrix[i][j]
            it+=1
        return [upper_sum,lower_sum]