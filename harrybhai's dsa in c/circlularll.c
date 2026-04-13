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
    
    printf("linked list before insertion\n");
    traversal(head);
    
    // after insertion 
    printf("linked list after insertion\n");
    head=insertatfirst(head,54);
    traversal(head);
    return 0;
}