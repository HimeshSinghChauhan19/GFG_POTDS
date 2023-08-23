class Solution {
public:
	vector<vector<int>>searchWord(vector<vector<char>>grid, string word){
	    /*
	    The main logic of this code is just like we humans look for a word in a grid, we just look for the first char of the word, and 
	    then look for all directions from that char, if we can get the word or not, so the steps are like;
	    1) look for the first char of the word, if found, then 
	    2) look up, down, left, right, upper left, upper right, lower left, lower right, from char, the main, thing is to take care of the 
	        boundaries while lookin for the word in these directions, we don't wanna cross the boundary of the grid and get a segmentation fault
	    3) If we get a match in either direction then just done for that position, we don't want a mathc in any other direction from that place, 
	       move to the other positions in the grid, 
	    4) Repeat the steps 
	    
	    (Apart from this, the comments should be sufficient to understand the code)
	    */
	    
	    
	    int n=grid.size(),m=grid[0].size();
	    vector<vector<int>> ans;
	    int wordSize=word.size();
	    
	    for(int i=0;i<n;i++){
	        for(int j=0;j<m;j++){
	            
	            if(grid[i][j]==word[0]){
	               // cout<<"Hey! Found an "<<word[0]<<" at the position "<<i<<","<<j<<endl;  
	                 
	                vector<int> temp(2);
	                int found=false;
	                 
	                // Upper Elems: if not at the first row
                    if(i!=0){
	                int count=0;
                        int itr=0;
                        for(int k=i;k>=0;k--){
                            if(grid[k][j]==word[itr++]){
                                count+=1;
                            }
                            else{
                                // if the word is not matched just ignore this case, try some other
                                // lower, or left or somethin
                                break;
                            }
                            
                            if(count==wordSize){
                                temp[0]=i;
                                temp[1]=j;
                                ans.push_back(temp);
                                found=true;
                                break;        
                            }
                            
                        }
                    }
                    
                    if(found==true){
                        // go on to look for some other coordinate, this one is done
                        continue;
                    }
                    // Lower Elems: if not at the last row
                    if(i!=n-1){
	                int count=0;
                        int itr=0;
                        
                        for(int k=i;k<=n-1;k++){
                            if(grid[k][j]==word[itr++]){
                                count+=1;
                            }
                            else{
                                break;
                            }
                            if(count==wordSize){
                                temp[0]=i;
                                temp[1]=j;
                                ans.push_back(temp);
                                found=true;
                                break;        
                            }
                            
                        }
                        
                    }
                    
                    if(found==true){
                        // go on to look for some other coordinate, this one is done
                        continue;
                    }
                    
                    // Left Elems: if not at the first column
                    if(j!=0){
	                    
                        int count=0;
                        int itr=0;
                        for(int k=j;k>=0;k--){
                            if(grid[i][k]==word[itr++]){
                                count+=1;
                            }
                            else{
                                break;
                            }
                            if(count==wordSize){
                                temp[0]=i;
                                temp[1]=j;
                                ans.push_back(temp);
                                found=true;
                                break;        
                            }
                            
                        }
                        
                    }
                    
                    if(found==true){
                        // go on to look for some other coordinate, this one is done
                        continue;
                    }
                    
                    // Right Elems: if not at the last column
                    if(j!=m-1){
	                int count=0;
                        // cout<<"We must be here...\n";
                        int itr=0;
                        for(int k=j;k<=m;k++){
                            if(grid[i][k]==word[itr++]){
                                count+=1;
                            }
                            else{
                                break;
                            }
                            if(count==wordSize){
                                // cout<<"Would have got the match here...\n";
                                temp[0]=i;
                                temp[1]=j;
                                // cout<<"Saved "<<i<<","<<j<<endl;
                                // cout<<"count: "<<count<<" and wordSize: "<<wordSize<<endl;
                                ans.push_back(temp);
                                found=true;
                                break;        
                            }
                            
                        }
                        
                    }
                    
                    if(found==true){
                        // go on to look for some other coordinate, this one is done
                        continue;
                    }
                    
                    // Upper Left Elems: if not at the top row and the leftmost column
                    if(j!=0 and i!=0){
	                int count=0;
                        int itr=0;
                         for(int k=0;k>-1;k++){
                            // Boundary Condition 
                            if(i-k<0 or j-k<0){
                                break;
                            }
                            
                            if(grid[i-k][j-k]==word[itr++]){
                                count+=1;
                            }
                            else{
                                break;
                            }
                            if(count==wordSize){
                                temp[0]=i;
                                temp[1]=j;
                                ans.push_back(temp);
                                found=true;
                                break;        
                            }
                            
                        }
                        
                    }
                    
                    if(found==true){
                        // go on to look for some other coordinate, this one is done
                        continue;
                    }
                    
                    // Upper Right Elems: if not at the top row and the rightmost column
                    if(j!=m-1 and i!=0){
                        
	                int count=0;
                        int itr=0;
                        for(int k=0;k>-1;k++){
                            // Boundary Condition
                            if(i-k<0 or j+k>m-1){
                                break;
                            }
                            
                            if(grid[i-k][j+k]==word[itr++]){
                                count+=1;
                            }
                            else{
                                break;
                            }
                            if(count==wordSize){
                                temp[0]=i;
                                temp[1]=j;
                                ans.push_back(temp);
                                found=true;
                                break;        
                            }
                            
                        }
                        
                    }
                    
                    if(found==true){
                        // go on to look for some other coordinate, this one is done
                        continue;
                    }
                    
                    // Lower Left Elems: if not at the bottom row and the leftmost col
                    if(j!=0 and i!=n-1){
                        
	                int count=0;
                        int itr=0;
                        for(int k=0;k>-1;k++){
                            // Boundary Condition
                            if(i+k>n-1 or j-k<0){
                                break;
                            }
                            
                            if(grid[i+k][j-k]==word[itr++]){
                                count+=1;
                            }
                            else{
                                break;
                            }
                            if(count==wordSize){
                                temp[0]=i;
                                temp[1]=j;
                                ans.push_back(temp);
                                found=true;
                                break;        
                            }
                            
                        }
                        
                    }
                    
                    if(found==true){
                        // go on to look for some other coordinate, this one is done
                        continue;
                    }
                    
                    // Lower Right Elems: if not at the bottom row and the rightmost col
                    if(j!=m-1 and i!=n-1){
                        
	                int count=0;
                        int itr=0;
                        for(int k=0;k>-1;k++){
                            // Boundary Condition
                            if(i+k>n-1 or j+k>m-1){
                                break;
                            }
                            
                            if(grid[i+k][j+k]==word[itr++]){
                                count+=1;
                            }
                            else{
                                break;
                            }
                            if(count==wordSize){
                                temp[0]=i;
                                temp[1]=j;
                                ans.push_back(temp);
                                found=true;
                                break;        
                            }
                            
                        }
                        
                    }
                    
                    if(found==true){
                        // go on to look for some other coordinate, this one is done
                        continue;
                    }
	            }
	            
	        }
	    }
	    return ans;
	}
};
