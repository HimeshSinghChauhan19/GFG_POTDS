class Solution{
    public:
    // Function to find equilibrium point in the array.
    // a: input array
    // n: size of array
    int equilibriumPoint(long long a[], int n) {
        

        long long total_sum=0,curr_sum=0;
        
        for(int i=0;i<n;i++){
            total_sum+=a[i];
        }
        
        for(int i=0;i<n;i++){
            
            curr_sum+=a[i];
            if((curr_sum-a[i])==(total_sum-curr_sum)){
                return i+1;
            }
        }
        
        return -1;
        
    }

};