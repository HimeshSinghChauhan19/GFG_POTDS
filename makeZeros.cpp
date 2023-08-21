class Solution {
public:
    void MakeZeros(vector<vector<int> >& matrix) {
        // Code here
        int n=matrix.size(),m=matrix[0].size();
        vector<vector<int>> temp(matrix);
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                int elem=temp[i][j];
                if(elem==0){
                    int summation=0;
                    
                    // Cases:
                    
                    if(i!=0){
                            summation+=temp[i-1][j];
                            matrix[i-1][j]=0;
                    }
                    
                    if(i!=n-1){
                            summation+=temp[i+1][j];
                            matrix[i+1][j]=0;
                    }
                    
                    if(j!=0){
                            summation+=temp[i][j-1];
                            matrix[i][j-1]=0;
                    }
                    
                    if(j!=m-1){
                            summation+=temp[i][j+1];
                            matrix[i][j+1]=0;
                    }
                    matrix[i][j]=summation;
                  
                }
            }
        }
    }
};