class Solution
{
    public:
    //Function to find minimum number of operations that are required 
    //to make the matrix beautiful.
        int findMinOpeartion(vector<vector<int> > matrix, int n)
    {
        // code here  
        int ans=0;
        // Getting the max summation, that will be the required summation for every row, and column
        int maxSum=-1,mxRow=-1,mxCol=-1;
        // string maxRow,maxCol;
        
        vector<int> rowsSummation(n);
        vector<int> colsSummation(n);
        
        for(int i=0;i<n;i++){
            int rowSummation=0,colSummation=0;
            // will compare the rows' and columns' sums separately and then will get the max one
            for(int j=0;j<n;j++){
                // ith row
                rowSummation+=matrix[i][j];
                
                
                // ith column
                colSummation+=matrix[j][i];
            }
            rowsSummation[i]=rowSummation;
            colsSummation[i]=colSummation;
            
            
            if(rowSummation>mxRow){
                mxRow=rowSummation;
                
            }
            if(colSummation>mxCol){
                mxCol=colSummation;
            }
            
        }
        if(mxRow>mxCol){
            maxSum=mxRow;    
        }
        else if(mxCol>mxRow){
            maxSum=mxCol;
        }
        else{
            // When they are both equal, then will go for row
            maxSum=mxRow;
        }
        
        
        // cout<<maxSum<<endl;
        // till here got the max summation
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                int rowS=0,colS=0;
                // checking the current position's row summation and col summation
                // for(int k=0;k<n;k++){
                //     // getting the row summation
                //     rowS+=matrix[i][k];
                    
                //     // getting the col summation
                //     colS+=matrix[k][j];
                // }
                // without the above loop, using predefined arrays to reduce the above work
                rowS=rowsSummation[i];
                colS=colsSummation[j];
                
                if(rowS==maxSum or colS==maxSum){
                    // then don't touch this elem
                    continue;    
                }
                
                // will take the one which would have a smaller difference from maxSum
                int rowDiff=maxSum-rowS,colDiff=maxSum-colS;
                
                // the changes made will contribute to the ans variable
                if((rowDiff)>(colDiff)){
                    
                    // if diff of col is less than rows'
                    // will increase the currentElem by maxSum-colS
                    matrix[i][j]+=colDiff;
                    ans+=colDiff;
                    
                    rowsSummation[i]+=colDiff;
                    colsSummation[j]+=colDiff;
                    
                }
                else{
                    
                    // will run for rowDiff<colDiff and also for rowDiff==colDiff, both are fine
                    matrix[i][j]+=rowDiff;
                    ans+=rowDiff;
                    
                    rowsSummation[i]+=rowDiff;
                    colsSummation[j]+=rowDiff;
                    
                }
                
                
            }
        }
        return ans;
    } 
};