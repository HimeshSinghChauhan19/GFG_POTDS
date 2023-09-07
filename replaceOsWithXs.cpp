class Solution{
public:
    
    void explore(int i,int j,int n,int m,vector<vector<char>>& mat){
        if(i<0 or i>=n or j>=m or j<0){
            return;
        }
        if(mat[i][j]=='X'){
            return;
        }
        if(mat[i][j]=='Z'){
            return;
        }
        mat[i][j]='Z';
        explore(i-1,j,n,m,mat);
        explore(i+1,j,n,m,mat);
        explore(i,j-1,n,m,mat);
        explore(i,j+1,n,m,mat);
    }

    vector<vector<char>> fill(int n, int m, vector<vector<char>> mat)
    {
        // code here
        
        // will just explore the O's whenever will find them in the boundary 
        // and will make them -1, then after all this, will traverse through the 
        // whole matrix and if I get an O, means it wasn't connected to any boundary O
        // so make it X, and change the -1 back to O
        for(int i=0;i<n;i++){
            // Will check for the two left and right boundaries in this loop
            if(mat[i][0]=='O'){
                // cout<<"Uno 'O'"<<endl;
                explore(i,0,n,m,mat);
            }
            if(mat[n-1-i][m-1]=='O'){
                // cout<<"Uno 'O'"<<endl;
                explore(n-1-i,m-1,n,m,mat);
            }
        }
        for(int j=0;j<m;j++){
            // will check for the upper and lower boundaries here
            if(mat[0][j]=='O'){
                // cout<<"Uno 'O'"<<endl;
                explore(0,j,n,m,mat);
            }
            if(mat[n-1][m-1-j]=='O'){
                // cout<<"Uno 'O'"<<endl;
                explore(n-1,m-1-j,n,m,mat);
            }
        }
        
        for(int i=0;i<n;i++){
            
            for(int j=0;j<m;j++){
                if(mat[i][j]=='Z'){
                    mat[i][j]='O';
                }
                else if(mat[i][j]=='O'){
                    mat[i][j]='X';
                }
            }
        }
        return mat;
        
    }
};