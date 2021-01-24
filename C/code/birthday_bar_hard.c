#include<stdio.h>
#include<stdlib.h>

int n, d, m;

int nested_sum(int curr_sum, int start, int end,  int* array, int depth, int final_depth, int target_count, int* result_count) {
    printf("start of round: %d at depth %d\n", curr_sum, depth);
    for (int i=start; i<end; i++) {
        int round_sum = curr_sum + *(array+i);
        printf("here we go with addition: %d\n", round_sum);
        if (depth == final_depth) {
            if (round_sum == target_count) {
                printf("match!\n");
                *result_count += 1;
            }
        }
        else {
            printf("    we are going down one layer\n");
            nested_sum(round_sum, start+1, end, array, depth+1, final_depth, target_count, result_count);
        }
    }
    return *result_count;
}

int result_count;


int main() {

    // load in data
    scanf("%d", &n);

    int* bs = malloc(n * sizeof(int));
    for (int i=0; i < n; i++) {
        scanf("%d", &*(bs + i));
    }

    scanf("%d", &d);
    scanf("%d", &m);

    // search for combinations
    int start_sum = 0;
    int initial_depth = 1;
    result_count = nested_sum(start_sum, 0, n, bs, initial_depth, m, d, &result_count);
    printf("Final result: %d\n", result_count);
}
