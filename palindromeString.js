class Solution {
    
    isPalindrome(S){
        //code here
        for(let i=0;i<parseInt(S.length/2);i++){
            if(S[i]!=S[S.length-1-i]){
                return 0;
            }
        }
        return 1;
    }
}