#include <stdlib.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    if (argc < 2) 
    {
        return 1;
    }

    int n;

    sscanf(argv[1], "%d", &n);
    
    if (n < 0)
    {
        return 2;
    }

    //printf("%d\n", n);

    int *p = malloc(n * sizeof(int));

    //printf("alloc done\n");

    if (argc == 3)
    {
        int m;

        sscanf(argv[2], "%d", &m);

        if (m < 0 || m > n)
        {
            free(p);
            
            return 3;
        }

        //printf("%d\n", m);

        for (int i = 0 ; i < m ; i++)
        {
            p[i] = 8;
        }

        //printf("write done\n");
    }
    
    free(p);
    
    return 0;
}
