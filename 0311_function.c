#include <stdio.h>
#include <stdlib.h>
double avg(int n1,int n2)
{
    double ans;
    ans = (n1+n2)/2.0;
    return ans;
}
int main()
{
    double average;
    average = avg(98,80);
    printf("%f",average);
    return 0;
}
// 9 > 11 > 12 > 3 > 5 > 6 > 7 > 12 > 13
