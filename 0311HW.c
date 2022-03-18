#include <stdio.h>
#include <stdlib.h>
int getMax(int a,int b,int c)
{
    int num = 0;
    if(a > num)
    {
        num = a;
    }
    if(b>num)
    {
        num = b;
    }
    if(c>num)
    {
        num = c;
    }
    return num;
}

int main()
{
    //HW1. 撰寫一個程式，讓使用者輸入6個整數，存成2*3的矩陣，再轉置成3*2的矩陣。
    /*
    int a,b,c,d,e,f;
    printf("請輸入六個整數並以空白區隔:\n");
    scanf("%d %d %d %d %d %d",&a,&b,&c,&d,&e,&f);

    printf("-----------2*3矩陣如下-----------\n");
    int matrix[2][3]={{a,b,c},{d,e,f}};

    for(int i=0;i<2;i++)
    {
        for(int j=0;j<3;j++)
        {
            printf("%d\t",matrix[i][j]);
        }
        printf("\n");
    }

    printf("-----------轉置矩陣如下-----------\n");
    int inverse[3][2];
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<2;j++)
        {
            inverse[i][j] = matrix[j][i];
            printf("%d\t",inverse[i][j]);
        }
        printf("\n");
    }
    */

    //HW2. 利用自定義函式的方式，讓使用者輸入三個正整數，並顯示三數中最大的值。

    int input1,input2,input3,answer;
    printf("請輸入三個整數並以空白區隔:\n");
    scanf("%d %d %d",&input1,&input2,&input3);
    answer = getMax(input1,input2,input3);
    printf("最大值為:%d\n",answer);


    return 0;
}
