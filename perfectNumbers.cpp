class Solution {
  public:
    int isPerfectNumber(long long N) {
        // code here
        long long sum=0;
        
        for(long long i=1;i<sqrt(N);i++){

            if(N%i==0){
                if(N/i==i){
                    sum+=i;
                }
                else{
                    sum+=i;
                    sum+=N/i;
                }
            }
        }
        
        // cout<<"sum is "<<sum<<endl;
        if(sum-N==N){
            return 1;    
        }
        else{
            return 0;
        }
    }
};