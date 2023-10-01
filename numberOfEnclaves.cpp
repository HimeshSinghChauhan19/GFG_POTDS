class Solution {
  public:
  
    // Will just explore the bondary 1's and those connected to them, n make them -1
    void explore(vector<vector<int>> &grid,int i,int j){
        // Will check for all the 4 sides keeping in mind the boundations
        
        // If we have visited this pos (i,j) means this is 1 for sure so make it -1
        grid[i][j]=-1;
        // Upper 
        if(i!=0 and grid[i-1][j]==1){
            explore(grid,i-1,j);
        }
        
        // Lower
        if(i!=grid.size()-1 and grid[i+1][j]==1){
            explore(grid,i+1,j);
        }
        
        // left
        if(j!=0 and grid[i][j-1]==1){
            explore(grid,i,j-1);
        }
        
        // right
        if(j!=grid[0].size()-1 and grid[i][j+1]==1){
            explore(grid,i,j+1);
        }
    }
    
    int numberOfEnclaves(vector<vector<int>> &grid) {
        // Code here
        int rows=grid.size(),columns=grid[0].size();
        
        // first and the last column
        for(int i=0;i<rows;i++){
            
            if(grid[i][0]==1){
                explore(grid,i,0);
            }
            if(grid[i][columns-1]==1){
                explore(grid,i,columns-1);
            }
        }
        // Now both the first and the last row
        for(int i=0;i<columns;i++){
            if(grid[0][i]==1){
                explore(grid,0,i);
            }
            if(grid[rows-1][i]==1){
                explore(grid,rows-1,i);
            }
        }
        
        int landCellCount=0;
        // now at this pt. will have the valid ones as 1 and the invalid land cells
        // as -1, so just need to count the number of 1's in the grid
        for(int i=0;i<rows;i++){
            for(int j=0;j<columns;j++){
                if(grid[i][j]==1){
                    landCellCount+=1;
                }
            }
        }
        return landCellCount;
    }
};