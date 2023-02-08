#include <iostream>
#include <unistd.h>

using namespace std;

static const int NB_ALLOCS = 1000;
static const int ALLOC_SIZE = 1000;

int main() {
        char ** array_of_arrays = (char**)malloc(NB_ALLOCS * sizeof(char *));
        for (int i = 0; i < NB_ALLOCS; i++) {
                //cout << "going to malloc" << endl;
                array_of_arrays[i] = (char *)malloc(ALLOC_SIZE);
        }
        cout << "Alloc done" << endl;
        sleep(0.1);
        cout << "Now writting" << endl;
        for (int i = 0; i < NB_ALLOCS; i++)
        {
                for (int j = 0; j < ALLOC_SIZE; j++) {
                        array_of_arrays[i][j] = 42;
                }
        }
        cout << "Done writting" << endl;
        sleep(0.1);
}
