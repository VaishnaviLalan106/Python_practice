#include<stdio.h>

int linearsearch(int arr[],int size,int element){
    for(int i=0;i<size;i++){
        if(arr[i]==element){
            return i;
        }
    }
    return -1;
}

int main(){
    int arr[]={1,56,23,6,2,12,78,9,90,4,256,890};
    int size=sizeof(arr)/sizeof(int);
    int element=7;
    int search=linearsearch(arr,size,element);
    printf("the element %d is at index %d",element,search);
    return 0;
}