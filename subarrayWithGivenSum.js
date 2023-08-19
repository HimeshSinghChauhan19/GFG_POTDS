class Solution 
{
    //Function to find a continuous sub-array which adds up to a given number.
    subarraySum(arr, n, s)
    {
        
        
        
        // for(let i=0;i<n;i++){
        //     let summation=arr[i];
        //     if(summation==s){
        //         return [i+1,i+1];
        //     }
        //     for(let j=i+1;j<n;j++){
        //         summation+=arr[j];
        //         if(summation==s){
        //             return [i+1,j+1];
        //         }
        //     }
        // }
        // return [-1];
        
        
        
        
        
        
        
        //your code here
        // let ans=new Array();
        let ans=[];
        let left=0,right=0;
        let summation=arr[0];
        // for(let i=0;i<n;i++){
        // arr.sort((a,b)=>(a-b));
        
        // let i=0;
        while(left<n && right<n){
            // console.log(arr[i++]);
            // if(i==n){
            //     break;
            // }
            // continue;
            if(s==0){
                return [-1];
            }
            if(summation==s){
                ans.push(left+1);
                ans.push(right+1);
                return ans;
            }
            else if(summation<s){
                // increment right, cause it
                right++;
                if(right==n){
                    return [-1];
                }
                summation+=arr[right];
                
                // if(summation==s){
                //     ans.push(left+1);
                //     ans.push(right+1);
                //     return ans;
                // }
            }
            else{
                // left++;
                if((left+1)==n){
                    return [-1];
                }
                summation-=arr[left++];
                
                // if(summation==s){
                //     ans.push(left+1);
                //     ans.push(right+1);
                //     return ans;
                // }
            }
            
        }
        // if I get to this place, means the sum s wasn't found in the array, so just return -1
        return [-1];
        
    }
}