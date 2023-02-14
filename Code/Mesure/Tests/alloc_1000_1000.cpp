#include <iostream>
#include <vector>

int main() {
    
    // Allocation de 1000Mo de mémoire virtuelle
    char* alloc = (char*) malloc(1000 * 1024 * 1024);

    // Utilisation de 1000 Mo de mémoire 
    for(int i = 0; i < 1000 * 1024 * 1024 ; i++) {
        alloc[i] = 'a';
    }

    // Libération de la mémoire
    free(alloc);

    return 0;

}