#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int NB_ALLOCS = 200;
    void *ptr[NB_ALLOCS];

    for (int i = 0; i < NB_ALLOCS; i++) {
        ptr[i] = malloc(50 * 1024 * 1024);
    }

    for (int i = 0; i < NB_ALLOCS; i++) {
        free(ptr[i]);
    }

    return 0;
}