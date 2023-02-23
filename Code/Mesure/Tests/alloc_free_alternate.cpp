#include <iostream>

int main() {
    int n = 100;
    void *ptr;
    
    for (int i = 0; i < n; i++) {
        ptr = malloc(100 * 1024 * 1024); // allocation de 100Mo
        free(ptr);                       // libération de la mémoire allouée
    }
    
    return 0;
}