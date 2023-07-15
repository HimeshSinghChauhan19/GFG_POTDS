class Solution 
{
    //Function to delete middle element of a stack.
    deleteMid(s, sizeOfStack)
    {
        // code here
        let midInd=Math.ceil((sizeOfStack+1)/2)-1;
        // console.log(midInd);
        let newStack= new Stack();
        let indFromStart=sizeOfStack-(midInd+1);
        
        for(let i=0;i<sizeOfStack;i++){
            if(i==indFromStart){
                continue;
            }
            newStack.push(s.a[i]);
        }
        s.a=newStack.a;
        // console.log(s);
    }
}