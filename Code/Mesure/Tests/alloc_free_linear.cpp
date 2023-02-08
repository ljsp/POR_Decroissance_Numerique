#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int NB_ALLOCS = 1000;
    void *ptr[NB_ALLOCS];

    for (int i = 0; i < NB_ALLOCS; i++) {
        ptr[i] = malloc(100 * 1024 * 1024);
    }

    for (int i = 0; i < NB_ALLOCS; i++) {
        free(ptr[i]);
    }

    return 0;
}