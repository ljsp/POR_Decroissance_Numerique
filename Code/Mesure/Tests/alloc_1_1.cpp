#include <iostream>

int main() {

    // Allocation de 1Mo de mémoire virtuelle
    char* alloc = (char*) malloc(1 * 1024 * 1024);

    // Utilisation de 1 Mo de mémoire 
    for(int i = 0; i < 1 * 1024 * 1024 ; i++) {
        alloc[i] = 'a';
    }

    // Libération de la mémoire
    free(alloc);

    return 0;

}