#include <stdio.h>
#include <stdlib.h>
/*
void swap(int *n1,int *n2)
{
    printf("n1=%d\tn2=%d\n",*n1,*n2);
    int temp;
    temp = *n1;
    *n1 = *n2;
    *n2 = temp;
    printf("n1=%d\tn2=%d\n",*n1,*n2);
}
int main()
{
    int a = 10,b = 20;
    printf("a=%d\tb=%d\n",a,b);

    swap(&a,&b);
    printf("a=%d\tb=%d\n",a,b);

    return 0;
}
*/
/*
int main()
{
    // 利用指標移動，算一維陣列的加總

    int arr[] = {10,20,30};
    int sum = 0;
    int *ptr = &arr;
    //int *ptr = &arr[0];

    //方法1
    //sum = *ptr + *(ptr+1) + *(ptr+2);
    //printf("%d",sum);

    //方法2
    for(int i=0;i<3;i++)
    {
        sum = sum + *(ptr+i);
    }
    printf("%d",sum);

    return 0;
}
*/
