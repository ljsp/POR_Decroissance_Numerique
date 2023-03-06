import sys
import array

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    
    n = int(sys.argv[1])

    if n < 0:
        exit(2)
    
    #print(n)

    p = array.array('i', (0 for i in range(0, n)))

    #print("alloc done")

    if len(sys.argv) == 3:
        m = int(sys.argv[2])

        if m < 0 or m > n:
            exit(3)
        
        #print(m)
        
        for i in range(m):
            p[i] = 8
        
        #print("write done")
    
    exit(0)
