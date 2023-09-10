// return the Kth largest element in the given BST rooted at 'root'
class Solution
{
    public:
    int kthLargest(Node *root, int K)
    {
        //Your code here
        int* ptr=&K;
        int ans=-1;
        int* ansPtr=&ans;
        solve(root,ptr,ansPtr);
        // cout<<K<<endl;
        return *ansPtr;
    }
    void solve(Node* root,int* ptr,int* ans){
        if(root!=NULL){
            solve(root->right,ptr,ans);
            if(*ptr==1){
                // cout<<"k is "<<*ptr<<" and data: "<<root->data<<endl;
                *ans=root->data;
                *ptr=-1;
                return;
            }
            (*ptr)--;
            solve(root->left,ptr,ans);
        }
    }
};