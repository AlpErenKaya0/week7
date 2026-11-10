#include <stdio.h>
#include <omp.h>

int main(void)
{
    int cost[8] = {1, 1, 1, 1, 8, 8, 8, 8};
    long long results[8] = {0};

    #pragma omp parallel for num_threads(4) schedule(___, 1)
    for (int i = 0; i < 8; i++) {

        // Simulate tasks with different amounts of work.
        long long local = 0;

        for (int j = 0; j < cost[i] * 100000; j++) {
            local += j % 7;
        }

        // Each iteration writes to a different element.
        results[i] = local;
    }

    long long total = 0;

    for (int i = 0; i < 8; i++) {
        total += results[i];
    }

    printf("Total: %lld\n", total);
    return 0;
}