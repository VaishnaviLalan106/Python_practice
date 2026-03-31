#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node* next;
};

void LinkedlistTraversal(struct Node* ptr){
    while(ptr!=NULL){
        printf("Element:%d\n",ptr->data);
        ptr=ptr->next;
    }
}
// case 1
struct Node * insertatfirst(struct Node * head,int data){
    struct Node * ptr=(struct Node *)malloc(sizeof(struct Node));
    ptr->data=data;
    ptr->next=head;
    return ptr;
}

// case 3
struct Node * insertatend(struct Node * head,int data){
    struct Node * ptr=(struct Node *)malloc(sizeof(struct Node));
    ptr->data=data;
    struct Node * p = head;
    while(p->next!=NULL){
        p=p->next;
    }
    p->next=ptr;
    ptr->next=NULL;
    return head;
}
 
// case 4
struct Node * insertafteranode(struct Node * head,struct Node * prevNode, int data){
    struct Node * ptr=(struct Node *)malloc(sizeof(struct Node));
    ptr->data=data;
    ptr->next=prevNode->next;
    prevNode->next=ptr;
    return head;
}
// case 2
struct Node * insertatindex(struct Node * head,int data,int index){
    struct Node * ptr=(struct Node *)malloc(sizeof(struct Node));
    struct Node * p = head;
    int i =0;
    while(i!=index-1){
        p=p->next;
        i++;
    }
    ptr->data=data;
    ptr->next=p->next;
    p->next=ptr;
    return head;
}

int main(){
    struct Node* head;
    struct Node* second;
    struct Node* third;
    struct Node* fourth;

    head = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    fourth = (struct Node*)malloc(sizeof(struct Node));

    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = fourth;
    
    fourth->data = 4;
    fourth->next = NULL;
    
    LinkedlistTraversal(head);
    // insert at first
    head=insertatfirst(head,0);
    printf("\n");
    LinkedlistTraversal(head); 

    // insert at index
     printf("\n");
    head=insertatindex(head,6,3);
    LinkedlistTraversal(head); 

    // insert at end
     printf("\n");
    head=insertatend(head,5);
    LinkedlistTraversal(head); 

    // insert after a node
    printf("\n");
    head=insertafteranode(head,second,7);
    LinkedlistTraversal(head);
    return 0;
}