#include <iostream>

int main(int argc, char const *argv[])
{
    if (argc < 2) 
        return 1;

    int n;
    sscanf(argv[1], "%d", &n);
    
    if (n < 0)
        return 2;
    std::cout << n << std::endl;

    char *p = (char*) malloc(n * sizeof(char));
    std::cout << "alloc done" << std::endl;

    if (argc == 3)
    {
        int m;
        sscanf(argv[2], "%d", &m);

        if (m < 0 || m > n)
        {
            free(p);
            return 3;
        }
        std::cout << m << std::endl;

        for (int i = 0 ; i < m ; i++)
            p[i] = 'a';
        std::cout << "write done" << std::endl;

        int i = 0;
        while (p[i] == 'a')
            i++;
        
        std::cout << "i = " << i << std::endl;
    }

    free(p);
    return 0;
}
