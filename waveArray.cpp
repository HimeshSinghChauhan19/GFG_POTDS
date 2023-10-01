class Solution{
    public:
    // arr: input array
    // n: size of array
    //Function to sort the array into a wave-like array.
    void convertToWave(int n, vector<int>& arr){
        // there's no catch in this problem it's just simple swap every 2 elems
        
        int i=0;
        while(i<n){
            if(i<=n-2){
                /* this is an interesting way to swap 2 elems but won't be 
                   working here cause the arr is containing ints and they won't
                   be able to handle 10^7+10^7.
                */
                // arr[i]=arr[i]+arr[i+1];
                // arr[i+1]=arr[i]-arr[i+1];
                // arr[i]=arr[i]-arr[i+1];
                
                // Means we can Swap this current element(ith elem) with the next
                int temp=arr[i];
                arr[i]=arr[i+1];
                arr[i+1]=temp;
            }
            else{
                // We cannot swap the curr elem with the next one
            }
            i+=2;
        }
        
    }
};