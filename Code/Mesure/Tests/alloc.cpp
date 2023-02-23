#include <iostream>
#include <vector>
#include <unistd.h>


int main() {
    // 10 Allocations de 50Mo de mémoire virtuelle
    for (int j = 0; j < 10; j++) {

    char* alloc = (char*) malloc(50 * 1024 * 1024);

    // Utilisation de 25 Mo de mémoire 
    for(int i = 0; i < 25 * 1024 * 1024; i++) {
        alloc[i] = 'a';
    }

    //sleep(1);
    
    // Libération de la mémoire
    free(alloc);
    }

    return 0;

}