class Solution {
  public:
    long long dp[1001][1001];
    // long long int getCount(int coins[],int ind,int total,vector<vector<long long>> dp){
    long long int getCount(int coins[],int ind,int total){
        // cout<<"We are here...\n";
        // return 1;
        // if(total==0){
        //     return 1;
        // }
        
        if(ind==0){
            if(total%coins[ind]==0){
                return 1;
            }
            else{
                return 0;
            }
        }
        
        if(dp[ind][total]!=-1){
            return dp[ind][total];
        }
        
        long long ignore=0,take=0;
        ignore=getCount(coins,ind-1,total);
        
        if(coins[ind]<=total){
            take=getCount(coins,ind,total-coins[ind]);
        }
        
        dp[ind][total]=ignore+take;
        return dp[ind][total];
    }
    
    long long int count(int coins[], int N, int sum){
        // int dp[N][sum+1];
        // filling the dp with all -1s in the class
        memset(dp,-1,sizeof(dp));
        
        /* The vectors are really slow compared to the memset function alongwith a 2D array */
        
        // vector<vector<long long>> dp(N,vector<long long>(sum+1,-1));
        // return getCount(coins,N-1,sum,dp);
        
        return getCount(coins,N-1,sum);
    }
};