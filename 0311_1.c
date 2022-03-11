#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    //宣告一個5格的整數陣列，初始化任意數字，算出陣列總和
    /*int num[5]={100,55,20};
    int sum = 0;
    for(int index=0;index<5;index++)
    {
        sum = sum+num[index];
        //sum += num[index];
    }
    printf("%d",sum);*/
/*
    int seat[2][3];
    for(int i=0;i<2;i++) //row
    {
        for(int j=0;j<3;j++) //c
        {
            printf("%d\t",seat[i][j]);
        }
        printf("\n");
    }
    */
    /*
    int index = 0;
    char name[] = "CAT";
    //字串方式印出
    printf("%s\n",name);
    //字元方式印出
    while(1)
    {
        if(name[index]!='\0')
        {
            printf("%c",name[index]);
            index++;
        }
        else{
            break;
        }
    }*/
    srand(time(NULL));
    int num;
    num = rand();
    printf("%d",num);


    return 0;
}
