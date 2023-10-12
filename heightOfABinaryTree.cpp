class Solution{
    public:
    int getHeight(Node* root){
        if(root==NULL){
            return 0;
        }
        
        return max(getHeight(root->left)+1,getHeight(root->right)+1);
    }
    //Function to find the height of a binary tree.
    int height(struct Node* node){
        // code here
        return getHeight(node);
    }
};