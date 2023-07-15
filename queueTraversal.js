class Solution {
    //Function to reverse the queue.
    rev(q)
    {
        let ans=new Queue();
        for(let i=q.arr.length-1;i>-1;i--){
            ans.push(q.arr[i]);
        }
        return ans;
    }
}