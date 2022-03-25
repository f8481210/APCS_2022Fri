#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char *str1 = "This is a book.";
    char *str2 = "aaa";
    // 字串的輸入、輸出 scanf printf fgets puts
    // 字串長度 strlen 不會算\0
    int temp = strlen(str1);
    //printf("%d",temp);
    // 字串合併全部合併 strcat(s1,s2) s2合併到s1
    // 字串合併指定位置 strncat(s1,s2,n) s2的前n個字合併進s1
    // 字串複製全部複製 strcpy(s2,s1) s1複製到s2裡
    // 字串複製指定位置 strncpy(s2,s1,n) s1前n個字複製到s2裡
    // 字串比較 strcmp(s1,s2) 前>後 return 1 / 前==後 return 0 / 前<後 return -1

    // 指標進行宣告
    // 字串搜尋字串 strstr(s1,s2) 回傳出現s2的第一個位置
    // 字串搜尋字元 strchr(s1,c) 回傳出現c的第一個位置
    char *str3=NULL;
    str3 = strstr(str1,str2);
    printf("%s",str3);

    return 0;
}
