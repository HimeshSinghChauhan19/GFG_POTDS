
class Solution {
    
    reverseWord(str){
        //Your code here
        
        
        // let arr1=new Array(...str);
        // console.log(arr1.reverse().join(""));
        // Just making an array from the string chars, so that reverse func
        // can be used and then join the elems of the array by an empty str
        return [...str].reverse().join("");
    }
}