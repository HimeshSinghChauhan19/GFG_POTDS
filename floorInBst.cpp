int ANS=0;
class Solution{

public:
    void inOrder(Node* root,int* num,int x){
        if(root!=NULL){
            inOrder(root->left,num,x);
            if(root->data<=x and abs(x-(root->data))<(*num)){
                *num=abs(x-(root->data));
                ANS=root->data;
            }
            inOrder(root->right,num,x);
        }
    }
    int floor(Node* root, int x) {
        // Code here
        // Everytime the ANS global var will be -1 by default, cause if there
        // would be no number <= x then the ans will be -1
        ANS=-1;
        int num=INT_MAX;
        int* ptr=&num; 
        // passing the pointer to num and will be used to get the num that 
        // will be closest to x provided that it is <=x too.
        inOrder(root,ptr,x);
        return ANS;
    }
};