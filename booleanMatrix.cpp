class Solution
{   
    public:
    //Function to modify the matrix such that if a matrix cell matrix[i][j]
    //is 1 then all the cells in its ith row and jth column will become 1.
    void booleanMatrix(vector<vector<int> > &matrix)
    {
        // code here 
        int rows=matrix.size(),cols=matrix[0].size();
        vector<int> dpRows(1000,0),dpCols(1000,0);
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(matrix[i][j]==1){
                    dpRows[i]=1;
                    dpCols[j]=1;
                }
            }
        }
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(dpRows[i]==1 or dpCols[j]==1){
                    matrix[i][j]=1;
                }
            }
        }
    }
};