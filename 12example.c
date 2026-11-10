#include <stdio.h>
#include <omp.h>

int main(void)
{
    int n = 3;
    int grid[4][4] = {0};

    // Initialize the boundary row and column.
    for (int i = 0; i <= n; i++) {
        grid[i][0] = 1;
        grid[0][i] = 1;
    }

    // All cells in a wave have i + j == wave.
    for (int wave = 2; wave <= 2 * n; wave++) {

        // Distribute this wave's cells across threads.
        ___
        for (int i = 1; i <= n; i++) {
            int j = ___;

            if (j >= 1 && j <= n) {
                grid[i][j] =
                    grid[i - 1][j] + grid[i][j - 1];
            }
        }

        // The parallel loop completes before the next wave starts.
    }

    printf("Result: %d\n", grid[n][n]);
    return 0;
}