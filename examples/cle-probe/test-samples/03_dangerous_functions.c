#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 危险函数样本: gets/strcpy/sprintf/strcat */
void dangerous_functions(void) {
    char buf[100];
    char dest[200];

    gets(buf);                    /* P0: gets 危险函数 */
    strcpy(dest, buf);            /* P1: strcpy 无边界 */
    sprintf(dest, "input: %s", buf);  /* P1: sprintf 无边界 */
    strcat(dest, buf);            /* P1: strcat 无边界 */

    printf("%s\n", dest);
}

int main(void) {
    dangerous_functions();
    return 0;
}
