#include<stdio.h>

void display(int arr[], int n){
    // traversal
    for (int i = 0; i < n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    
}

void indDeletion(int arr[], int size, int index){
    //deletion
      for (int i = index; i<size-1; i++)
      {
        arr[i]=arr[i+1];
      }
}

int main(){
    int arr[100] = {1,3,5,6,78};
    int size=5,index=1;
    display(arr,size);
    indDeletion(arr,size,index);
    size-=1;
    display(arr,size);
    return 0;
}