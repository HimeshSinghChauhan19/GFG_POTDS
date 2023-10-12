bool ANS_CONST=true;

class Solution{
    public:
    //Function to check whether a binary tree is balanced or not.
    int getHeight(Node* root){
        if(root==NULL){
            return 0;
        }
        int leftHeight=getHeight(root->left)+1;
        int rightHeight=getHeight(root->right)+1;
        if(abs(leftHeight-rightHeight)>=2){
            // return false;
            ANS_CONST=false;     
            // cout<<"must not be here...\n";
            return 0;
        }
        // cout<<abs(leftHeight-rightHeight)<<endl;
        return max(leftHeight,rightHeight);
    }
    
    bool isBalanced(Node *root)
    {
        // if(root->data==849 and root->left->data==96 and root->right->data==71){
        //     // cout<<"Are we here?\n";
        //     return 0;
        // }
        // cout<<abs(getHeight(root->left)-getHeight(root->right))<<endl;
        // return abs(getHeight(root->left)-getHeight(root->right))<=1;
        getHeight(root);
        if(ANS_CONST==false){
            // reset this for the next test case
            ANS_CONST=true;
            return false;
        }
        else{
            return true;
        }
    }
};