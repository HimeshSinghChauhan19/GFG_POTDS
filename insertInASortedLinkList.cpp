class Solution{
  public:
    // Should return head of the modified linked list
    Node *sortedInsert(struct Node* head, int data) {
        // Code here
        Node* it=head;
        Node* newNode=new Node(data);
        if(data<=head->data){
            newNode->next=head;
            return newNode;
        }
        while(it!=NULL){
            if(it->next==NULL and data>it->data){
                it->next=newNode;
                return head;
            }
            else if(it->data<=data and it->next->data>=data){
                newNode->next=it->next;
                it->next=newNode;
                return head;
            }
            it=it->next;
        }
        cout<<"Never gonna be here!\n";
    }
};