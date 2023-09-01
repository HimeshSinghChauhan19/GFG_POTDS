class Solution {
    // works fine, but there was some problem in the code of gfg, that was taking the 
    // input
  	printCorner(root){
  		//code here
    let queue=[]
    // heapq.heapify(queue)
    // heapq.heappush(queue,root)
    queue.unshift(root);
    // console.log(queue)
    while(queue.length!=0){
        let queueSize=queue.length;
        // console.log(queueSize)
        
        process.stdout.write(`${queue[0].data} `)
        
        if(queueSize!=1){
            process.stdout.write(`${queue[queueSize-1].data} `)
        }
        
        for(let i=0;i<queueSize;i++){
            
            let nodeTemp=queue.shift();
            // console.log(nodeTemp.data);
        
            if(nodeTemp.left!=null)
                queue.push(nodeTemp.left)
            
            if(nodeTemp.right!=null)
                queue.push(nodeTemp.right)    
        }
        
        
    }
  	}