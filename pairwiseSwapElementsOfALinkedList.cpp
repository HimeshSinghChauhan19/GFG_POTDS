class Solution
{
    public:
    Node* pairWiseSwap(struct Node* head) 
    {
        // The task is to complete this method
        Node* it=head;
        Node* prevNode=NULL;
        int count=0;
        Node* first=head;
        int once=0;
        Node* prevNode1=NULL;
        while(it!=NULL){
            Node* temp=it->next;
            
            if(count++%2==1){
                if(once==0){
                    once=1;
                    first=it;
                }
                else{
                    prevNode1->next=it;
                }
                prevNode->next=it->next;
                // cout<<it->data<<" ";
                it->next=prevNode;
                
            }
            else{
                prevNode1=prevNode;
                prevNode=it;
                
            }
            it=temp;
        }
        // cout<<endl;
        
        return first;
    }
};