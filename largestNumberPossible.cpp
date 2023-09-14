class Solution{
public:
    string findLargest(int N, int S){
        // code here
        if(S==0 and N==1){
            // this is the only thing we can return in this case
            return "0";
        }
        if(S==0){
            // if s is 0 and n is not 1, means n>1 and that is not possible
            return "-1";
        }
        
        string ans="";
        int isLeft=-1;
        for(int i=1;i<=N;i++){
            if(S==0){
                isLeft=i;
                break;
            }
            if(S>=10){
                ans+="9";
                S-=9;
            }    
            else{
                // here the s is <=9 and >=1, means it is a single digit so we 
                // can just take whatever is left that digit only
                int temp=S;
                string dig=to_string(temp);
                ans+=dig;
                // cout<<"S became 0 at digit "<<i<<endl;
                S=0;
            }
            
        }
        // if couldn't meet the summation requirement them just return -1
        if(S!=0){
            return "-1";
        }
        // If I gotta append 0's at the end, then this will take care of that
        if(isLeft!=-1){
            for(int i=isLeft;i<=N;i++){
                ans+="0";
            }
        }
        return ans;
    }
};