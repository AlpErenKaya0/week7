#include <stdio.h>
#include <omp.h>

int main(void)
{
    int values[4] = {0, 0, 0, 0};

    omp_set_dynamic(0);

    #pragma omp parallel num_threads(4) shared(values)
    {
        int id = omp_get_thread_num();

        values[id] = id + 1;

        // Wait until all threads have written their values.
        ___

        if (id == 0) {
            int total = values[0] + values[1]
                      + values[2] + values[3];

            printf("Total: %d\n", total);
        }
    }

    return 0;
}