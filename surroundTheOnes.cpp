class Solution {
public:
    int Count(vector<vector<int> >& matrix) {
        // Code here
        
        // for(auto i:matrix){
        //     for(auto j:i){
        //         cout<<j<<" ";
        //     }
        //     cout<<endl;
        // }
        // cout<<endl;
        
        int ans=0;
        int n=matrix.size(),m=matrix[0].size();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                // cout<<matrix[i][j]<<" ";
                int elem=matrix[i][j];
                
                if(elem==1){
                    int surroundCount=0;
                    
                    // Cases:
                    
                    // Upper Elems: if not at the first row
                    if(i!=0){
                        if(matrix[i-1][j]==0){
                            surroundCount+=1;
                        }
                    }
                    
                    // Lower Elems: if not at the last row
                    if(i!=n-1){
                        if(matrix[i+1][j]==0){
                            surroundCount+=1;
                        }
                    }
                    
                    // Left Elems: if not at the first column
                    if(j!=0){
                        if(matrix[i][j-1]==0){
                            surroundCount+=1;
                        }
                        
                    }
                    
                    // Right Elems: if not at the last column
                    if(j!=m-1){
                        if(matrix[i][j+1]==0){
                            surroundCount+=1;
                        }
                        
                    }
                    
                    // Upper Left Elems: if not at the top row and the leftmost column
                    if(j!=0 and i!=0){
                        if(matrix[i-1][j-1]==0){
                            surroundCount+=1;
                        }
                        
                    }
                    
                    // Upper Right Elems: if not at the top row and the rightmost column
                    if(j!=m-1 and i!=0){
                        if(matrix[i-1][j+1]==0){
                            surroundCount+=1;
                        }
                        
                    }
                    
                    // Lower Left Elems: if not at the bottom row and the leftmost col
                    if(j!=0 and i!=n-1){
                        if(matrix[i+1][j-1]==0){
                            surroundCount+=1;
                        }
                        
                    }
                    
                    // Lower Right Elems: if not at the bottom row and the rightmost col
                    if(j!=m-1 and i!=n-1){
                        if(matrix[i+1][j+1]==0){
                            surroundCount+=1;
                        }
                        
                    }
                    
                    // if the surroundCount is even till here, that means +1 for ans
                    if(surroundCount%2==0 and surroundCount!=0){
                        ans+=1;
                    }
                }
            }
            // cout<<endl;
        }
        // cout<<endl;
        return ans;
    }
};