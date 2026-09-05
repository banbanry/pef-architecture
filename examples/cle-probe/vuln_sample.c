#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 含漏洞样本: P0-1 malloc未检查NULL; P0-2 除零; P1-3 sprintf无边界 */
void process(char *input) {
    char *buf = (char *)malloc(1024);   /* P0: malloc 未检查 NULL */
    int divisor = 0;
    int x = 10;
    x = x / divisor;                     /* P0: 除零 */
    sprintf(buf, "data: %s", input);     /* P1: sprintf 无边界 */
    printf("%s", buf);
    free(buf);
}

int main(int argc, char **argv) {
    if (argc > 1) process(argv[1]);
    return 0;
}
