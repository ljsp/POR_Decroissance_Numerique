#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 100;
    void *ptr;
    
    for (int i = 0; i < n; i++) {
        ptr = malloc(100 * 1024 * 1024); // allocation de 1024 octets
        free(ptr); // libération de la mémoire allouée
    }
    
    return 0;
}