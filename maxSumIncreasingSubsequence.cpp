class Solution{
		

	public:
	int maxSumIS(int arr[], int n)  
	{  
	    // Your code goes here
	   //The recur+memo doesn't work for this bcz prob
	   // vector<vector<int>> dp(n, vector<int>(n+1,-1));
	   // return solveMem(0,-1,arr,n,dp);
	   
	   vector<int> dp(arr,arr+n);
	   //for(int i=0;i<dp.size();i++){
	   //    cout<<dp[i]<<" ";
	   //}
	   //cout<<endl;
	   int ans=-1;
	   for(int i=1;i<n;i++){
	       for(int j=i-1;j>=0;j--){
	           if(arr[j]<arr[i]){
	               dp[i]=max(dp[i],arr[i]+dp[j]);
	               if(dp[i]>ans){
	                   ans=dp[i];
	               }
	           }
	       }
	   }
	   
	   
	   for(int i=0;i<dp.size();i++){
	       //cout<<dp[i]<<" ";
	       if(dp[i]>ans)
	       ans=dp[i];
	   }
	   return ans;
	} 
};
