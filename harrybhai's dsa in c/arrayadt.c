#include<stdio.h>
#include<stdlib.h>
struct arrayadt 
{
    int total_size;
    int used_size;
    int *ptr;
};

void createArray(struct arrayadt * a,int tSize,int usize){
     /*(*a).total_size=tSize;
      (*a).used_size=usize;
      (*a).ptr=(int*)malloc(tSize*sizeof(int)) */
      a->total_size=tSize;
      a->used_size=usize;
      a->ptr=(int *)malloc(tSize*sizeof(int));
}
void show(struct arrayadt *a){
    for(int i=0;i<a->used_size;i++){
    printf("%d\n",(a->ptr)[i]);
    }
}
void setVal(struct arrayadt *a){
    int n;
    for(int i=0;i<a->used_size;i++){
    printf("Enter the element:",i);
    scanf("%d\n",&n);
    (a->ptr)[i]=n;
    }
}

int main()
{
    struct arrayadt marks;
    createArray(&marks,10,2);
    setVal(&marks);
    show(&marks);
    return 0;
}