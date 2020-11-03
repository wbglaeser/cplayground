#include <stdio.h>
#include <stdlib.h>

int* apples;
int* oranges;

int main() {

    int s, t, a, b, m, n;
    int pos;
    int apples_counter = 0;
    int oranges_counter = 0;

    scanf("%d", &s);
    scanf("%d", &t);
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &m);
    scanf("%d", &n);

    apples = malloc(m * sizeof(int));
    oranges = malloc(n * sizeof(int));

    printf("tree pos: %d\n", a);
    for (int j; j < m; j++) {
        scanf("%d", &pos);
        printf("rel position: %d\n",a+pos);
        if (a+pos >= s && a+pos <= t) {
            printf("condition met");
            apples_counter++;
        }
    }

    for (int j; j < n; j++) {
        scanf("%d", &pos);
        if (b+pos >= s && b+pos <= t) {
            apples_counter++;
        }
    }

    printf("%d\n", apples_counter);
    printf("%d\n", oranges_counter);

    return 0;
}
