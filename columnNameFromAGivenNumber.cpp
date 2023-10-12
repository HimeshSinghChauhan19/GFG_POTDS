class Solution{
    public:
    string colName (long long int n)
    {
        // your code here
        //for 28 we will get output as AB
        //according to this logic we will get characters in reverse order
        //so first we are adding character then we are adding result to it
        //by this newest character will be at begging
        //-->B  (27%26=1 in A when we add 1 WE GET B)
        //-->AB   (0%26=0 in A we will add 0==A)
     
          string ans="";
          while(n>0)
          {
              int pos=(n-1)%26;
              char ch='A'+pos;
              ans= ch+ans;
              n=(n-1)/26;
          }
        
          return ans;
        
       
    }
    
};