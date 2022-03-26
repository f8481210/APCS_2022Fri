#include <stdio.h>
#include <stdlib.h>
//定義一個結構名稱為student的結構，
//該結構含有學號姓名年齡，輸入多筆學生資料後印出。
struct student{
    char no[20];
    char name[10];
    int age;
};
int main()
{
    struct student arr[5];

    for(int i=0;i<5;i++)
    {
        printf("input no name age:");
        scanf("%s%s%d",&arr[i].no,&arr[i].name,&arr[i].age);
    }
    printf("no\tname\tage\n");
    for(int i=0;i<5;i++)
    {
        printf("%s\t%s\t%d\n",arr[i].no,arr[i].name,arr[i].age);
    }




    return 0;
}
