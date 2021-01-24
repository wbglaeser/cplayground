#include <stdio.h>
#include <stdlib.h>

int n, k;

int array_test(int n, int k, int* array) {
    int success = 1;
    for (int i; i < n; i++) {
        for (int j=i; j<n; j++) {
            int _sum = *(array+i) + *(array+j);
            if (_sum % k != 0 ) {
                success = 0;
                break;
            }
        }
        if (success == 0) { break; }
    }
    if (success == 0) { return 0; }
    else { return sizeof(*array)/sizeof(int); }
}

int* permutate_array(int n, int r, int* array) {
    
}

int main() {

    scanf("%d", &n);
    scanf("%d", &k);

    int* array = malloc(n * sizeof(int));
    for (int i; i < n; i++) {
        scanf("%d", &*(array+i));
    }



    // test for given array array


    return 0;
}
