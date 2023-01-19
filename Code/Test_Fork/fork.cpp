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
        // Allocation dynamique sur le tas 100Mo
        int* alloc = (int*) malloc(100 * 1024 * 1024);
        // Allocation sur la pile de 1Mo
        char buffer[1 * 1024 * 1024];
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