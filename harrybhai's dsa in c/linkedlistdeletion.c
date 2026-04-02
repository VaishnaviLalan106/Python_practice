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

// case 1
struct Node* deleteatfirst(struct Node * head){
    struct Node*ptr=head;
    head=head->next;
    free(ptr);
    return head;
}

//case 2
struct Node * deleteatindex(struct Node *head,int index){
    struct Node *p=head;
    struct Node *q=head->next;
    for(int i=0;i<index-1;i++){
        p=p->next;
        q=q->next;
    }
    p->next=q->next;
    free(q);
    return head;
}
//case 3
struct Node* deleteatend(struct Node * head){
    struct Node *p=head;
    struct Node *q =head->next;
    while(q->next!=NULL){
        p=p->next;
        q=q->next;
    }
    p->next=NULL;
    free(q);
    return head;
}
//case 4
struct Node* deleteatgivenvalue(struct Node * head,int value){
    struct Node *p=head;
    struct Node *q =head->next;
    while(q->data!=value && q->next!=NULL){
        p=p->next;
        q=q->next;
    }
    if(q->data==value){
        p->next=q->next;
        free(q);
    }
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

    // delete at index
    head=deleteatindex(head,3);
    LinkedlistTraversal(head);
    printf("\n"); 

    // delete at end
    head=deleteatend(head);
    LinkedlistTraversal(head);
    printf("\n"); 

    // delete a given value
    head=deleteatgivenvalue(head,21);
    LinkedlistTraversal(head);
    printf("\n");
    return 0;
}