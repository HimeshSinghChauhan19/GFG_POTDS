
class Solution
{
    public:
    void solve(Node* root,Node* newNode,int val){
        if(root!=NULL){
            if(val<root->data and root->left==NULL){
                root->left=newNode;
            }
            if(val>root->data and root->right==NULL){
                // cout<<"Are we here?\n";
                root->right=newNode;
            }
            if(val==root->data){
                return;
            }
            if(val<root->data){
                solve(root->left,newNode,val);
            }
            if(val>root->data){
                solve(root->right,newNode,val);
            }
        }
    }
    Node* insert(Node* node, int data) {
        
        Node* newNode=(Node*)malloc(sizeof(Node));
        newNode->data=data;
        newNode->left=NULL;
        newNode->right=NULL;
        
        // cout<< (newNode->data) <<end;
        solve(node,newNode,data);
        return node;
    }

};