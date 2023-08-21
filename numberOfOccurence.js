class Solution {
    
    count(arr,n,x){
        //code here
        /*
        The overall idea of this problem is that they want us to use binary search to keep getting 
        the elem whose frequency we need, that's the reason that the array given is sorted, 
        If you look at the Expected Time Complexity then, that is O(log n) well, the time complexity 
        of Binary Search, that's the only catch in this, they think that the average person
        would just go for the normal freuency getting method and would think that they are done
        with this, but that's where they would get a TLE, and the idea collapses, 
        now if you don't
        get this searching idea in your mind, then I don't think there is aay other way to handling 
        this.
        */
        
        // I am just gonna perform Binary Search till I keep getting the elem
        // and just update the elem value that is found to -1
        /*
        LOL, I just realised, that I didn't even think about this, 
        if we get the value for the first time, then obviously the value will be continuously
        placed if present more times as the array is sorted, like if 
        we gotta search for 4, 
        in arr: [1,2,2,2,3,4,4,4,23,34,34]
        so we don't have to do log n for n times, cz obviously that would become, n*logn
        how can I miss that, xd
        */
        
        let indOfX=-1,count=0;
        let mid,left=0,right=n-1;
        while(left<right){
            mid=parseInt((left+right)/2);
            if(arr[mid]==x){
                indOfX=mid;
                // break;
            }
            else if(arr[left]==x){
                indOfX=left;
                // break;
            }
            else if(arr[right]==x){
                indOfX=right;
                // break;
            }
            
            // conditional updates
            if(x>arr[mid]){
                left=mid+1;
            }
            else{
                // means x is < mid value
                right=mid-1;
            }
        }
        // at this point, will have the index of x elem
        // now just get the frequency
        
        // this below loop is there to handle 1 more catch, bcz I may not find the leftmost occurence
        // of the elem x, so I gotta get that to keep things simple, so i just get that and then 
        // go for getting the frequencies in a linear manner further in the last loop,
        let leftMost=indOfX;
        for(let i=indOfX;i>-1;i--){
            if(arr[i]!=x){
                break;
                
            }
            leftMost=i;
        }
        indOfX=leftMost;
        // console.log(indOfX);
        
        for(let i=indOfX;i<n;i++){
            if(arr[i]!=x){
                // means the continous x elems are over now
                break;
            }
            count++;
        }
        
        return (indOfX==-1)?0:count;
    }
}