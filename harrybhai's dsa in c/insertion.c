#include<stdio.h>

void display(int arr[], int n){
    // traversal
    for (int i = 0; i < n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    
}

int indInsertion(int arr[], int size, int element,int capacity,int index){
    //insertion
      if (size>=capacity){
        return -1;
      }
      for (int i = size-1; i>=index; i--)
      {
        arr[i+1]=arr[i];
      }
      arr[index]=element;
      return 1;
}

int main(){
    int arr[100] = {1,3,5,6,78};
    int size=5,element=45,index=4;
    display(arr,size);
    int result=indInsertion(arr,size,element,100,index);
    size+=1;
    if (result==1){
    display(arr,size);
    }
    else{
        printf("insertion was not succesful");
    }

    return 0;
}