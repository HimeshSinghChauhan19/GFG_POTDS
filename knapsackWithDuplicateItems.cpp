class Solution{
public:
    int t[1001][1001];
    
    int helper(int N, int W, int val[], int wt[])
    {
        if(N == 0 || W == 0) return 0;
        // cout<<"Got to "<<N-1<<" at left weight "<<W<<endl;
        if(t[N][W] != -1){
            // cout<<"On "<<N-1<<" at weight "<<W<<" stored is "<<t[N][W]<<endl;
            return t[N][W];
        }
        if(wt[N-1] <= W){
            return t[N][W] = max(val[N-1]+helper(N, W-wt[N-1], val, wt), helper(N-1, W, val, wt));
        }
        else{
            return t[N][W] = helper(N-1, W, val, wt);
        }
    }
    
    int knapSack(int N, int W, int val[], int wt[])
    {
        memset(t, -1, sizeof(t));
        return helper(N, W, val, wt);
    }
};