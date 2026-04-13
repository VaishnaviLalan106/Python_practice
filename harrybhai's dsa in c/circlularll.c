#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

void traversal(struct Node *head){
    struct Node *ptr=head;
    do{
        printf("Element:%d\n",ptr->data);
        ptr=ptr->next;
    }while(ptr!=head);
}

struct Node *insertatfirst(struct Node *head,int data){
    struct Node * ptr=(struct Node *)malloc(sizeof(struct Node));
    ptr->data=data;

    struct Node * p=head->next;
    while(p->next!=head){
        p=p->next;
    }
    // at this point p is pointing to the last node of circular linked list
    p->next=ptr;
    ptr->next=head;
    head=ptr;
    return head;
}

struct Node * insertatindex(struct Node * head,int data,int index){
    struct Node * ptr=(struct Node *)malloc(sizeof(struct Node));
    ptr->data=data;
    struct Node *p=head;
    int i=0;
    while(i!=index-1){
        p=p->next;
        i++;
    }
    ptr->next=p->next;
    p->next=ptr;
    return head;
}

struct Node * insertatend(struct Node *head,int data){
    struct Node *ptr=(struct Node*)malloc(sizeof(struct Node));
    ptr->data=data;
    struct Node *p =head;
    while(p->next!=head){
        p=p->next;
    }
    // here p is pointing to the last node of circular linked list
    p->next=ptr;
    ptr->next=head;
    return head;
}

struct Node * insertafternode(struct Node * head,struct Node * prevNode,int data){
    struct Node * ptr=(struct Node*)malloc(sizeof(struct Node));
    ptr->data=data;
    ptr->next=prevNode->next;
    prevNode->next=ptr;
    return head;
} 

int main(){
    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;

    //allocate memory for nodes in heap 
    head=(struct Node*)malloc(sizeof(struct Node));
    second=(struct Node*)malloc(sizeof(struct Node));
    third=(struct Node*)malloc(sizeof(struct Node));
    fourth=(struct Node*)malloc(sizeof(struct Node));


    // allocate data for head node
    head->data=7;
    head->next=second;

    // allocate data for second node
    second->data=11;
    second->next=third;

    // terminate in third node
    third->data=21;
    third->next=fourth;
    
    // to put fourth node and terminate it
    fourth->data=66;
    fourth->next=head;
    traversal(head);
    printf("\n");

    // insert at first
    head=insertatfirst(head,54);
    traversal(head);
    printf("\n"); 

    // insert at index
    head=insertatindex(head,45,3);
    traversal(head);
    printf("\n");

    // insert at end
    head=insertatend(head,23);
    traversal(head);
    printf("\n"); 

    // insert after a node
    head=insertafternode(head,second,12);
    traversal(head);
    printf("\n");

    return 0;
}