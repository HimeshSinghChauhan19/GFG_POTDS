leaders(arr, n){
    /* Fairly Self-Explanatory Algorithm */
    
    let ans=new Array(),rightGreatest=0;
    // console.log(ans);
    for(let i=arr.length-1;i>-1;i--){
        // console.log(arr[i]);
        if(arr[i]>=rightGreatest){
            // can either use, push with reverse at the end,
            // ans.push(arr[i]);
            
            // or use unshift to add the elems from the beginning of the array, as 
            // required by the problem statement
            ans.unshift(arr[i]);
        }
        // update the rightGreatest, cause now, arr[i] is also contributing to it for the next
        // left element if > rightGreatest
        // if(arr[i]>rightGreatest){
        //     rightGreatest=arr[i];
        // }
        
        // a ternary version of the above if condition,
        rightGreatest=((arr[i]>rightGreatest)?arr[i]:rightGreatest);
    }
    // console.log(`This is the length of the new array: ${ans.push(-1)}`);
    // console.log(`This is the popped element of the array: ${ans.pop(-1)}`);
    
    // if would have used push so would have had to reverse the ans array at the end,
    // ans.reverse();
    return ans;
}