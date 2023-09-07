class Solution
{
public:
    int getCount(Node *root, int k)
    {
        //code here
        int ansCount=0;
        queue<Node*> q1;
        q1.push(root);
        int level=1;
        while(q1.size()!=0){
            int n=q1.size();
            for(int i=0;i<n;i++){
                Node* node=q1.front();
                
                q1.pop();
                
                // cout<<node->data<<" ";
                
                if(node->left==NULL && node->right==NULL){
                    // Means this was a leaf node
                    
                    if((k-level)<0){
                        return ansCount;
                    }
                    else{
                        ansCount+=1;
                        k-=level;
                    }
                }
                
                if(node->left!=NULL){
                    q1.push(node->left);
                }
                if(node->right!=NULL){
                    q1.push(node->right);
                }
                
            }
            level++;
            // cout<<endl;
        }
        return ansCount;
    }
};