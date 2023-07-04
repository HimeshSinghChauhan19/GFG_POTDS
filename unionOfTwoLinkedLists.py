class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        temp=head1
        ls=list()
        new_ll=linkedList()
        while(temp!=None):
            # print(temp.data)
            ls.append(temp.data)
            temp=temp.next
        temp=head2
        while(temp!=None):
            # print(temp.data)
            ls.append(temp.data)
            temp=temp.next
        # while(len(ls)!=0):
        
        ls=list(set(ls))
        ls.sort()
        for i in range(len(ls)):
            # nod=Node(ls[i])
            new_ll.insert(ls[i])
        # print(head1)
        # print(head2)
        return new_ll.head