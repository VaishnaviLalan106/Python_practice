#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node * prev;
    struct Node * next;
};

void linkedlisttraversal(struct Node * head){
    struct Node * ptr=head;
    while(ptr!=NULL){
        printf("Element:%d\n",ptr->data);
        ptr=ptr->next;
    }
}

// case 1
struct Node * insertatfirst(struct Node * head,int data){
   struct Node * ptr=(struct Node *)malloc(sizeof(struct Node));
   ptr->data=data;
   struct Node *p=head;
   ptr->next=head;
   head->prev=ptr;
   ptr->prev=NULL;
   head=ptr;
   return head;
}

// case 3
struct Node * insertatend(struct Node * head,int data){
    struct Node * ptr=(struct Node *)malloc(sizeof(struct Node));
    ptr->data=data;
    struct Node *p=head;
    while(p->next!=NULL){
        p=p->next;
    }
    p->next=ptr;
    ptr->prev=p;
    ptr->next=NULL;
    return head;
}
 
// case 4
struct Node * insertafteranode(struct Node * head,struct Node * prevNode, int data){
    struct Node * ptr=(struct Node *)malloc(sizeof(struct Node));
    ptr->data=data;
    ptr->next=prevNode->next;
    prevNode->next->prev=ptr;
    prevNode->next=ptr;
    ptr->prev=prevNode;
    return head;
}
// case 2
struct Node * insertatindex(struct Node * head,int data,int index){
   struct Node *ptr=(struct Node *)malloc(sizeof(struct Node));
   struct Node *p=head;
   int i=0;
   while(i!=index-1){
    p=p->next;
    i++;
   }
   ptr->data=data;
   ptr->next=p->next;
   p->next->prev=ptr;
   p->next=ptr;
   ptr->prev=p;
   return head;
}

int main() {
    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;

    head=(struct Node*)malloc(sizeof(struct Node));
    second=(struct Node*)malloc(sizeof(struct Node));
    third=(struct Node*)malloc(sizeof(struct Node));
    fourth=(struct Node*)malloc(sizeof(struct Node));

    head->data=7;
    head->prev=NULL;
    head->next=second;

    second->data=11;
    second->prev=head;
    second->next=third;

    third->data=21;
    third->prev=second;
    third->next=fourth;

    fourth->data=66;
    fourth->prev=third;
    fourth->next=NULL;
    
    linkedlisttraversal(head);
    
    // insert at first
    head=insertatfirst(head,54);
    linkedlisttraversal(head);
    printf("\n");

    // insert at index
    head=insertatindex(head,45,3);
    linkedlisttraversal(head);
    printf("\n");

    // insert at end
    head=insertatend(head,23);
    linkedlisttraversal(head);
    printf("\n");

    // insert after a node
    head=insertafteranode(head,second,12);
    linkedlisttraversal(head);
    printf("\n");  
    return 0;
}