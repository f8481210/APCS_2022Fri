#include <stdio.h>
#include <stdlib.h>

struct student
{
    char name[20];
    char no[20];
    char age[5];
};
int main()
{
    struct student st[5]={0};
    int i;
    for(i = 0; i < 5; i++)
    {
        printf("請輸入學生資料：\n");
        printf("學生名字：\n");
        scanf("%s", &st[i].name);
        printf("學生NO：\n");
        scanf("%s", &st[i].no);
        printf("學生年齡：\n");
        scanf("%s", &st[i].age);
    }
    for(i=0;i<5;i++)
    {
        printf("%s %s %s\n", st[i].no, st[i].name, st[i].age);
    }

    printf("%d\n",i);


    return 0;
}

