class Solution{
  public:
    vector<int> printClosest(int arr[], int brr[], int n, int m, int x) {
        /* The overall idea is to use the 2 Pointer approach in both the arrays
            cause they are sorted so we can find the answer in O(n) only */
        
        int i=0,j=m-1,ans=INT_MAX;
        vector<int> ans_vect(2,0);
        // The normal 2 Pointer Approach
        // Just the change is that here the i and j can cross each other it doesnt' 
        // matter cause they are pointing to different arrays
        while(i<n and j>-1){
            long long summation=arr[i]+brr[j]; 
            long long difference=abs(summation-x);
            
            // Keep updating the answer var
            if(difference<ans){
                ans=difference;
                ans_vect[0]=arr[i];
                ans_vect[1]=brr[j];
            }
            // We wanna make the summation equal to x
            if(summation<x){
                // Mean we need to increase the summation
                i+=1;
                continue;
            }
            if(summation>x){
                // Means wanna decrease
                j-=1;
                continue;
            }
            if(summation==x){
                // If the summation is x only, so we got the best answer
                return {arr[i],brr[j]};
            }
        }
        return ans_vect;
        
    }
};