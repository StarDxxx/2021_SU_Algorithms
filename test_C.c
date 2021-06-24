#include <stdio.h>

void function(int *x) {
    printf("==Begin==");
    printf("x_id: %d, x_value: %d\n", x, *x);
    *x = NULL;
    printf("==After==");
    printf("x_id: %d, x_value: %d\n", x, *x);
}

int main(void) {
    int x = 1;

    printf("x_id: %d, x_value: %d\n", x, &x);
    function(&x);
    return 0;
}