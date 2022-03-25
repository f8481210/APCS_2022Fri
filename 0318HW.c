#include <stdio.h>
#include <stdlib.h>

//撰寫一個程式，建立兩個不同尺寸的整數陣列，
//傳至sumTwoArray()函式內，利用指標計算陣列的總和，
//並在主程式將答案印出。

// & 取址運算子 * 取值運算子
int sumTwoArray(int *arr1,int *arr2)
{
    int *ptr1 = arr1;
    int *ptr2 = arr2;
    int temp=0;

    //arr1 sum
    for(int i=0;i<3;i++)
    {
        //temp = temp + (*ptr1)+1;
        //temp = temp + *ptr1++;
        temp += *ptr1++;
    }
    //printf("arr1 = %d\n",temp);
    //arr2 sum
    for(int i=0;i<4;i++)
    {
        temp += *ptr2++;
    }
    return temp;

}
int main()
{
    int arr1[3]={1,2,3},arr2[4]={4,5,6,7};
    int ans;

    ans = sumTwoArray(&arr1,&arr2);

    printf("arr1+arr2 = %d",ans);
    return 0;
}


