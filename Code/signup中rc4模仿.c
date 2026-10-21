
#include <stdio.h>
#include <windows.h>
#include<string.h>
int main(void) {
    SetConsoleOutputCP(CP_UTF8);   // 输出按 UTF-8 解码
SetConsoleCP(CP_UTF8);
    char soul[64];
    printf("请输入：");
    if (fgets(soul, sizeof(soul), stdin) == NULL)   // 最多 6 字符
        return 1;
    soul[strcspn(soul, "\n")] = '\0';              // 去掉换行
    printf("你真的做对了吗%s\n", soul);
    return 0;
}

















