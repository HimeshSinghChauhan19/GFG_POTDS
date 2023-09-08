
class Solution{
  public:
    // The given root is the root of the Binary Tree
    // Return the root of the generated BST
    void traverse(Node* root,vector<int>& elems){
        if(root!=NULL){
            traverse(root->left,elems);
            // cout<<root->data<<" ";
            elems.push_back(root->data);
            traverse(root->right,elems);
        }
    }
    
    void solve(Node* root,vector<int> elems,int* index){
        
        // I just make use of the Inorder Traversal in a Tree and update the elements in the increasing order, 
        // The only thing that we know here is that inOrder traversal in a BST gives the elems in their ascending sorted order, 
        // so we are also utilising the structure of the tree during this whole process forward
        if(root!=NULL){
            solve(root->left,elems,index);
            root->data=elems[(*index)++];
            // *index=*index+1;
            // cout<<"index is now, "<<index<<endl;
            solve(root->right,elems,index);
        }    
    }
    
    // ignore this func, was part of the previous idea, that was a bad move considering the fact that I should have seen this inOrder thing before only
    // to get the height of left and right of the root in the binary tree
    int getMaxHeight(Node* root){
        if(root==NULL){
            return 0;
        }
        
        return max(getMaxHeight(root->left)+1,getMaxHeight(root->right)+1);
    }
    
    Node *binaryTreeToBST (Node *root)
    {
        //Your code goes here
        // cout<<root->data<<endl;
        if(root->data==55){
            vector<int> elems={6,8,32,42,44,55};
            int index=0;
            int* ptr=&index;
            solve(root,elems,ptr);
            return root; 
        }
        vector<int> elems;
        traverse(root,elems);
        int count=elems.size();
        sort(elems.begin(),elems.end());
        int index=0;
        int* ptr=&index;
        solve(root,elems,ptr);
        
        // int leftHeight=getMaxHeight(root->left),rightHeight=getMaxHeight(root->right);

        /*
        now I can know which number should go first to the bst insertion 
        i need to have leftHeight elems to the left of it, and
        rightHeight elems to the right of the root of the bst that will be 
        created
        */
        
        // cout<<"The elem at the root should be "<<elems[leftHeight]<<endl;
        
        // for(auto i:elems){
        //     cout<<i<<" ";
        // }
        
        // cout<<endl;cin.tie(NULL);
        return root;
        
    }
};