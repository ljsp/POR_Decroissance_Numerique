#include <iostream>
#include <vector>

int main() {
    // Allocation de 100Mo de mémoire virtuelle
    std::vector<char> v(50 * 1024 *1024);

    int* alloc = (int*) malloc(50 * 1024 * 1024);

    // Utilisation de 25 Mo de mémoire 
    for(int i = 0; i < 25 * 1024 * 1024; i++) {
        v[i] = 'a';
    }

    return 0;

}