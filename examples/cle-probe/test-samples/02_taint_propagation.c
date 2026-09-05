#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 污点传播样本: scanf输入直达system命令 */
void execute_user_cmd(char *input) {
    char cmd[256];
    scanf("%s", cmd);           /* P1: scanf %s 无边界 */
    system(cmd);                 /* P0: 命令注入（污点直达system） */
}

void taint_chain(char *user_input) {
    char buf[128];
    strcpy(buf, user_input);     /* P1: strcpy 无边界 */
    printf(buf);                  /* P1: 格式字符串漏洞 */
}

int main(int argc, char **argv) {
    if (argc > 1) {
        execute_user_cmd(argv[1]);
        taint_chain(argv[1]);
    }
    return 0;
}
