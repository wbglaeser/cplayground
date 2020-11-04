#include <stdio.h>
#include <stdlib.h>

int main() {

    int k1, v1, k2, v2;

    scanf("%d", &k1);
    scanf("%d", &v1);
    scanf("%d", &k2);
    scanf("%d", &v2);

    int diff = abs(k1 - k2);
    int counter = 0;

    while( 1 ) {

        k1 += v1;
        k2 += v2;

        if ( abs(k1 - k2) >= abs(diff) ) {
            printf("NO");
            break;
        } else if (abs(k1 - k2) == 0) {
            printf("YES");
            break;
        }

    }

    return 0;
}
