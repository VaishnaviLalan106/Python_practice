#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

void LinkedlistTraversal(struct Node* ptr){
    while(ptr!=NULL){
        printf("Element:%d\n",ptr->data);
        ptr=ptr->next;
    }
}

struct Node* deleteatfirst(struct Node * head){
    struct Node*ptr=head;
    head=head->next;
    free(ptr);
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
    fourth->next=NULL;

    LinkedlistTraversal(head);
    printf("\n");
    // delete at first
    head=deleteatfirst(head);
    LinkedlistTraversal(head);
    printf("\n");

    return 0;
}