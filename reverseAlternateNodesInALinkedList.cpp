class Solution
{
    public:
    void rearrange(struct Node *odd)
    {
        //add code here
        // Node* temp= new (struct Node)(0);
        // Node* prev_normal=new Node(0);
        // Node* prev_alter=new Node(0);
        
        
        Node* it=odd;
        Node* temp=NULL;
        Node* prev_normal=it;
        Node* prev_alter=NULL;
        
        int count=1;
        while(it!=NULL){
            
            temp=it->next;
            
            
            if(count%2==0){
                // When there's an alternative node
                
                if(prev_alter!=NULL){
                    // making a reverse chain of the alter nodes
                    it->next=prev_alter; 
                    // now next time will make the alter node point to this one
                    prev_alter=it;
                    
                }
                else{
                    prev_alter=it;
                    // bcz this will be the last node of the resulting LL
                    prev_alter->next=NULL;
                    
                }
            }
            else{
                // otherwise
                if(prev_normal!=NULL){
                    // cout<<"At 9: "<<it->data<<endl;
                    // cout<<"Making "<<prev_normal->data<<" point to "<<it->data<<endl;
                    prev_normal->next=it;   
                }
                
                prev_normal=it;
                
            }
            
            
            count++;
            it=temp;    

        }
        // joining the normal node LL with the LL having alter nodes in reverse
        prev_normal->next=prev_alter;

    }
};