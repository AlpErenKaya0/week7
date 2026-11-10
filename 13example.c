#include <stdio.h>
#include <omp.h>

int main(void)
{
    int a[8];
    int b[8];

    #pragma omp parallel num_threads(4)
    {
        // Remove the unnecessary barrier after this loop.
        #pragma omp for ___
        for (int i = 0; i < 8; i++) {
            a[i] = i * 2;
        }

        // This loop does not depend on the first loop.
        #pragma omp for
        for (int i = 0; i < 8; i++) {
            b[i] = i + 10;
        }
    }

    // Both arrays are ready after the parallel region.
    printf("a[7] = %d, b[7] = %d\n", a[7], b[7]);

    return 0;
}