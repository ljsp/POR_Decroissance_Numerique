#!/bin/sh
#-*-mode:c-*-
(echo "#line 3 \"$0\"";echo;tail -n +4 $0) >/tmp/cs.$$.c && gcc -Wall -o /tmp/cs.$$ /tmp/cs.$$.c && /tmp/cs.$$ $*;rm -f /tmp/cs.$$*; exit

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int size=10;
    int full=5;
    if(argc>1)
    {
        size=atoi(argv[1]);
        assert(size>0);
    }
    if(argc>2)
    {
        full=atoi(argv[2]);
        assert(full>0);
    }
    char * data=malloc(size);
    size_t p=getpagesize();
    printf("size=%x=%d, "
           "full=%x=%d "
           "(%d%%)\n",
           size,size,full,full,
           (int)(100.0*full/size));
    for(int i=0 ; i<full;i+=p)
    {
        data[i]=42;
        printf("%x\n",i);
    }
    return 0;
}


