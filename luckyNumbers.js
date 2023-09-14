
class Solution {
    isLucky(n)
    {
        // code here
        for(let i=2;i<=n;i++){
            if(n%i==0){
                return false;
            }
            
            n-=Math.floor(n/i);
        }
        return true;
    }
}