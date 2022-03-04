#include <stdio.h>
#include <stdlib.h>

int main()
{
    //HW1
    int c=128;
    /*double f;
    f = (double)c * 9 / 5 + 32;
    printf("攝氏%d度  = 華氏 %f 度\n",c,f);*/
    printf("攝氏%d度  = 華氏 %f 度\n",c,(double)c * 9 / 5 + 32);

    //HW2
    float h = 10.84,x = 25.6;
    printf("三角形的底為%.2lf 高為%.2lf，面積等於 %.2lf\n",x,h,x * h / 2);

    //HW3
    int y,z;
    printf("number:");
    scanf("%d%d",&z,&y);
    printf("%d + %d = %d\n", z, y, z + y);
	printf("%d - %d = %d\n", z, y, z - y);
	printf("%d * %d = %d\n", z, y, z * y);
	printf("%d / %d = %f\n", z, y, (float)z / (float)y);
	printf("%d %% %d = %d\n", z, y, z % y);
}
