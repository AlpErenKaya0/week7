#include <stdio.h>
#include <omp.h>

int main(void)
{
    int counter = 0;

    omp_set_dynamic(0);

    #pragma omp parallel num_threads(4) shared(counter)
    {
        // Make this single update atomic.
        ___
        counter++;
    }

    printf("Counter: %d\n", counter);
    return 0;
}