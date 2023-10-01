class Solution
{   
    public:
    //Function to return list of integers that form the boundary 
    //traversal of the matrix in a clockwise manner.
    vector<int> boundaryTraversal(vector<vector<int> > matrix, int n, int m) 
    {
        vector<int> ans;
        // code here
        
        // traversing the 1st row
        for(int i=0;i<m;i++){
            ans.push_back(matrix[0][i]);
        }
        
        // traversing the last column
        for(int i=1;i<n;i++){
            ans.push_back(matrix[i][m-1]);
        }
        
        // Only if there is more than 1 row, cause with just 1 row that row will
        // be repeated twice, 
        
        // Traversing the last row
        if(n!=1){
            for(int i=1;i<m;i++){
                if((m-1-i)<0){
                    cout<<"Must be here...\n";
                    break;
                }
                ans.push_back(matrix[n-1][m-1-i]);
            }
        }
        
        // only if there is more than 1 column, same reason just with cols
        
        // Traversing the 1st Column
        if(m!=1){
            for(int i=1;i<n-1;i++){
                if((n-1-i)<0){
                    cout<<"Must be here too...\n";
                    break;
                }
                ans.push_back(matrix[n-1-i][0]);
            }
        }
        return ans;
    }
};