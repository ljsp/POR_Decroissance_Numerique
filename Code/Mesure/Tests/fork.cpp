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
        // Allocation de 50Mo de mémoire virtuelle
        char* alloc = (char*) malloc(50 * 1024 * 1024);

        // Utilisation de 25 Mo de mémoire 
        for(int i = 0; i < 25 * 1024 * 1024; i++) {
            alloc[i] = 'a';
        }

        free(alloc);
        std::cout << "printed from child process " << getpid() << std::endl;
        exit(EXIT_SUCCESS);
    }

    return EXIT_SUCCESS;
}