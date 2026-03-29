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

int main(){
    struct Node *head;
    struct Node *second;
    struct Node *third;

    //allocate memory for nodes in heap 
    head=(struct Node*)malloc(sizeof(struct Node));
    second=(struct Node*)malloc(sizeof(struct Node));
    third=(struct Node*)malloc(sizeof(struct Node));

    // allocate data for head node
    head->data=7;
    head->next=second;

    // allocate data for second node
    second->data=11;
    second->next=third;

    // terminate in third node
    third->data=66;
    third->next=NULL;
    LinkedlistTraversal(head);
    return 0;
}