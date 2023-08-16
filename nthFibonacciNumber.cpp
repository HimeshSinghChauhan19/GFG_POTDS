class Solution {
  public:
    long long nthFibonacci(long long n){
        // code here
        long long a=1,b=1,c;
            
        for(long long i=1;i<=n;i++){
            if(i==n){
                return a%1000000007;
            }
            // cout<<a<<endl;
            c=(a+b)%1000000007;
            a=b;
            b=c;
        }
        return -1;
    }
};