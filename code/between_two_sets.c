#include <stdio.h>
#include <stdlib.h>

int a_len, b_len;

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main() {

    scanf("%d", &a_len);
    scanf("%d", &b_len);

    int* a = malloc(a_len * sizeof(int));
    int* b = malloc(b_len * sizeof(int));

    for (int i; i < a_len; i++) {
        scanf("%d", &*(a+i));
    }

    for (int i; i < b_len; i++) {
        scanf("%d", &*(b+i));
    }

    int a_max = 0;
    for (int i=0; i<a_len; i++) {
        if (*(a+i) > a_max) {a_max=*(a+i);}
    }

    int b_min = 100;
    for (int i=0; i<b_len; i++) {
        if (*(b+i) < b_min) {b_min=*(b+i);}
    }

    int match_counter = 0;
    for (int i = a_max; i <= b_min; i++) {

        int invalid = 0;
        for(int ai=0; ai < a_len; ai++) {

            int int_div = i / *(a + ai);
            float float_div = (float)i / (float)*(a + ai);

            if ( (float)int_div - float_div != 0.) {
                invalid = 1;
                break;
            }
        }
        if (invalid == 1) {continue;}

        for (int bi=0; bi < b_len; bi++) {

            if ( *(b + bi) % i != 0) {
                invalid = 1;
                break;
            }
        }

        if (invalid == 1) {continue;}
        match_counter++;
    }

    printf("%d\n", match_counter);

    return 0;
}
