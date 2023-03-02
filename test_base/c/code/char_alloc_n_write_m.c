#include <stdlib.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    if (argc < 2) 
        return 1;

    int n;
    sscanf(argv[1], "%d", &n);
    
    if (n < 0)
        return 2;

    char *p = (char*) malloc(n);

    if (argc == 3)
    {
        int m;
        sscanf(argv[2], "%d", &m);

        if (m < 0 || m > n)
        {
            free(p);
            return 3;
        }

        for (int i = 0 ; i < m ; i++)
            p[i] = 'a';
    }
    
    free(p);
    return 0;
}
