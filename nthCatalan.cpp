class Solution
{
    public:
    //Function to find the nth catalan number.
    long long dp[10000];
    
    Solution(){
        memset(dp,0,sizeof(dp));
    }
    
    long long findCatalan(int n) 
    {
        //code here
        if(n<=1){
            return 1;
        }
        dp[0]=1;
        dp[1]=1;
        
        if(dp[n]!=0){
            return dp[n]%1000000007;
        }
        for(int i=2;i<n+1;i++){
            for(int j=0;j<i;j++){
                dp[i]+=findCatalan(j)*findCatalan(i-j-1);
                dp[i]=dp[i]%1000000007;
            }
        }
        long long divisor=1000000007;
        dp[n]=dp[n]%divisor;
        return dp[n];
    }
};