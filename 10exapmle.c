#include <stdio.h>
#include <omp.h>

int main(void)
{
    int balance = 0;
    int updates = 0;

    omp_set_dynamic(0);

    #pragma omp parallel num_threads(4) shared(balance, updates)
    {
        // Allow only one thread at a time inside this block.
        ___
        {
            balance += 10;
            updates++;
        }
    }

    printf("Balance: %d, updates: %d\n", balance, updates);
    return 0;
}