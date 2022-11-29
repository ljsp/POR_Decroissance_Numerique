#include <iostream>
#include <sys/wait.h>
#include <unistd.h>

// g++ -o run main.cpp
// strace -o empty_main.txt -f -ff -e trace=mmap ./run

// Test Fork
int main() {
    pid_t c_pid = fork();

    if (c_pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (c_pid > 0) {
        std::cout << "printed from parent process " << getpid() << std::endl;
        wait(nullptr);
    } else {
        // Allocation dynamique sur le tas
        int* alloc = (int*) malloc(1000 * sizeof(int));
        // Allocation sur la pile
        int hello = 42;
        std::cout << "printed from child process " << getpid() << std::endl;
        exit(EXIT_SUCCESS);
    }

    return EXIT_SUCCESS;
}

// Test Allocation
/*
int main() {
    int * alloc = (int*) malloc(8 * sizeof(int));
    std::cout << "Allocation dynamique sur le tas" << std::endl;
}*/

// Test main vide
/*
int main() {

}
*/