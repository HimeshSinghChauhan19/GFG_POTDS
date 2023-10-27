class Solution{
public:
    int t[501][501]; //Cache memory for fast response
    
    // Just a normal function for checking palindrome
    bool isPalin(string &s, int i, int j){
        while(i <= j){
            if(s[i++] != s[j--]) return false;
        }
        return true;
    }

    int helper(string &s, int i, int j){
        if(i >= j) return 0; // If there are no elements, then no partition needed.
        
        if(t[i][j] != -1) return t[i][j]; // If subproblem is already calculated, then that from there
        
        if(isPalin(s, i, j)) return 0; // If already is a palindrome, then no need to partitioning.
        
        int mini = INT_MAX; // Mini variable for calculating, the minimum value
        
        // Checking for all possibilities of partitioning, like - MCM
        for(int k=i;k<=j-1;k++){
            // increament by '1', for the track the no. of partition
            // int ans = 1 + helper(s, i, k) + helper(s, k+1, j);
            int left,right;
            if(t[i][k]!=-1){
                left=t[i][k];
            }
            else{
                left=helper(s,i,k);
            }
            if(t[k+1][j]!=-1){
                right=t[k+1][j];
            }
            else{
                right=helper(s,k+1,j);
            }
            
            int ans=1+left+right;
            // Update Minimum Variable
            mini =min(mini, ans);
        }
        return t[i][j] = mini; // Store and return our answer
    }

    int palindromicPartition(string str){
        memset(t, -1, sizeof(t)); //Initialize cache memory with all '-1'
        return helper(str, 0, str.size()-1);
    }
};
