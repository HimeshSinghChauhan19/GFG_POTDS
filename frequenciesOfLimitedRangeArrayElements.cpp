class Solution{
    public:
    //Function to count the frequency of all elements from 1 to N in the array.
    void frequencyCount(vector<int>& arr,int N, int P)
    { 
        // code here
        // int mx=-1;
        // for(int i=0;i<N;i++){
        //     if(arr[i]>mx){
        //         mx=arr[i];
        //     }
        // }
        vector<int> freqs(N,0);
        for(int i=0;i<N;i++){
            if(arr[i]<=N){
                freqs[arr[i]-1]+=1;
            }
        }
        for(int i=0;i<N;i++){
            arr[i]=freqs[i];
        }
    }
};