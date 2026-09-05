#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 硬编码密码 + 资源泄漏样本 */
#define ADMIN_PASSWORD "super_secret_123"  /* P1: 硬编码密码 */
#define API_KEY "sk-abcdef1234567890"      /* P1: 硬编码API密钥 */

int authenticate(char *user, char *pass) {
    FILE *fp = fopen("/etc/config", "r");  /* 资源：文件句柄 */
    char *buf = malloc(1024);                /* 资源：内存 */

    if (strcmp(pass, ADMIN_PASSWORD) == 0) {
        return 1;  /* 认证成功，但buf和fp未释放 */
    }
    /* P1: 资源泄漏 - fopen和malloc的资源在错误路径未释放 */
    return 0;
}

int main(void) {
    return authenticate("admin", "test");
}
