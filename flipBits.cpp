class Solution{
    public:
    int maxOnes(int a[], int n)
    {
        
        int one_count=0,count=0,max_count=0;
        // console.log(a);
        for(int i=0;i<n;i++){
            // console.log("Here?");
            // console.log(`i: ${i}`)
            if(a[i]==1){
                // console.log("Here?");
                
                one_count+=1;
                count-=1;
            }
            else{
                // means when it's a 0
                // console.log(`this was a 0: ${a[i]}`)
                count+=1;
            }
            if(count>max_count){
                max_count=count;
            }
            if(count<0){
                count=0;
            }
        }
        return max_count+one_count;
    }
};