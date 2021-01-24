#include<stdio.h>
#include<stdlib.h>

int n, d, m;

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
    int result_count;
    for (int i; i<n-m+1; i++){
        int round_sum=0;
        for (int j=i; j<i+m; j++){
            round_sum += *(bs + j);
        }
        if (round_sum == d) {
            result_count++;
        }
    }

    printf("%d\n", result_count);
}
