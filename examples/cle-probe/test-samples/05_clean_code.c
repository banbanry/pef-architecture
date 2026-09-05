#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 干净代码样本: 正确的错误处理和边界检查 */
#define BUF_SIZE 256

int safe_process(const char *input) {
    char *buf = (char *)malloc(BUF_SIZE);
    if (buf == NULL) {
        fprintf(stderr, "malloc failed\n");
        return -1;
    }

    int divisor = 10;
    if (divisor == 0) {
        free(buf);
        return -1;
    }
    int x = 100 / divisor;  /* 安全：除数有检查 */

    snprintf(buf, BUF_SIZE, "data: %s, x=%d", input, x);  /* 安全：snprintf有边界 */
    printf("%s\n", buf);

    free(buf);
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "usage: %s <input>\n", argv[0]);
        return 1;
    }
    return safe_process(argv[1]);
}
