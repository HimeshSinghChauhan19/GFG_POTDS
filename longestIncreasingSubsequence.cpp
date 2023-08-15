class Solution
{
    public:
    // int dp[10001][10001];
    int getLongestSub(int prevIndex,int ind,int arr[],int n){
        if(ind==n){
            return 0;
        }
        
        int take=-9999;
        int notTake=getLongestSub(prevIndex,ind+1,arr,n);
        
        if(prevIndex==-1){
            // cout<<"Will run only once\n";
            take=getLongestSub(ind,ind+1,arr,n)+1;
        }
        else if(arr[ind]>arr[prevIndex]){
            // cout<<"could take here...prevIndex:"<<prevIndex<<" and ind:"<<ind<<"\n";
            take=getLongestSub(ind,ind+1,arr,n)+1;
        }
        return max(take,notTake);
    }
    

    //Function to find length of longest increasing subsequence.
    int longestSubsequence(int n, int a[])
    {
        // memset(dp,-1,sizeof(dp));
        return getLongestSub(-1,0,a,n);    
    }
};