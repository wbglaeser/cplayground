#include <stdio.h>

int i, n, m, score;
int top, stack[200002];

int main() {
    // read n - the number of players on the leaderboard
    scanf("%d", &n);

    for (i = 0; i < n; ++i) {
        scanf("%d", &stack[top+1]);
        if (stack[top+1] != stack[top]) ++top;
    }

    // read m - the number of levels Alice beats
    scanf("%d", &m);

    // read Alice's scores and output the corresponding ranks
    for (i = 0; i < m; ++i) {
        // read a score
        scanf("%d", &score);
        while (top && score >= stack[top]) --top;

        // output the current rank
        printf("%d\n", top+1);
    }
    return 0;
}
