#include <stdio.h>
#include <stdlib.h>

int main()
{
    //HW1
    /*
    for(int i=1;i<=9;i++)
    {
        for(int j=1;j<=i;j++)
        {
            printf("%d",j);
        }
        //執行完一行要換行
        printf("\n");
    }*/

    //HW2
    float ch,e,m,s,se,avg;
    printf("請輸入國英數自社五科成績:");
    scanf("%f%f%f%f%f",&ch,&e,&m,&s,&se);
    avg = (ch+e+m+s+se)/5;
    printf("平均= %.2f",avg);

    //HW3
    int op,sum = 0,drink,x;
    printf("----- 簡易販售飲料系統 -----\n\n");
    while(1)
    {
        printf("1.飲料總覽\n2.購買飲料\n3.顯示目前消費金額\n4.結帳\n請輸入要使用的功能：");
        scanf("%d",&op);
        if(op == 4)
        {
            printf("消費總金額為:%d元\n請輸入收款金額:",sum);
            scanf("%d",x);
            printf("找零%d元",x-sum);
            break;
        }
        else if(op == 1)
        {
            printf("\n可樂 28元\t礦泉水 25元\t美式咖啡 45元\n\n");
        }
        else if(op==2)
        {
            printf("\n1.可樂 2.礦泉水 3.美式咖啡\n請問要購買的品項：");
            scanf("%d",&drink);
            if(drink==1)
            {
                sum+=28;
            }
            else if (drink==2)
            {
                sum+=25;
            }
            else
            {
                sum+=45;
            }
        }
        else if(op==3)
            printf("目前消費金額：%d\n\n",sum);
    }
    return 0;
}
