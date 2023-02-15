#include <iostream>
#include <vector>
#include <unistd.h>

int main() {
    
    // Allocation de 100Mo de mémoire virtuelle
    char* alloc = (char*) malloc(200 * 1024 * 1024);

    // Utilisation de 25 Mo de mémoire 
    for(int i = 0; i < 125 * 1024 * 1024 ; i++) {
        alloc[i] = 'a';
    }

    // Libération de la mémoire
    sleep(1);
    free(alloc);

    return 0;

}