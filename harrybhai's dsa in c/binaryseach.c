#include<stdio.h>

int binarysearch(int arr[],int size,int element){
    int low,mid,high;
    low=0;
    high=size-1;
    //searching starts here
    while(low<=high){
    mid=(low+high)/2;
    if (arr[mid]==element){
        return mid;
    }
    if (arr[mid]<element){
        low=mid+1;
    }
    else{
        high=mid-1;
    }
    //searching ends here
    }
    return -1;
}

int main(){
    //sorted array for binary search
    int arr[]={1,2,4,6,7,9,12,23,56,78,90,256,890};
    int size=sizeof(arr)/sizeof(int);
    int element=890;
    int search=binarysearch(arr,size,element);
    printf("the element %d is at index %d",element,search);
    return 0;
}