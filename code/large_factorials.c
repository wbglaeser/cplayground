#include <stdio.h>
#include <stdint.h>

int n;

int main() {

    // read n - the number of players on the leaderboard
    scanf("%d", &n);
    uint64_t big[100] = {0};
    int counter=1;
    big[0] = 1;

    for (int j=1; j <= n; j++) {

        int update =0;
        uint32_t carry=0;
        for(int i=0; i<=counter; i++) {

            uint64_t tmp = j * (uint64_t)big[i] + carry;
            big[i] = tmp % 1000000000;
            carry = tmp / 1000000000;

            if (carry && i == counter) {
                big[i + 1] = carry;
                update = 1;
            }
        }

        if (update) {counter++;}
    }

    if (counter == 1) {
      printf("%lu", (long)big[0]);
    } else {
      printf("%lu", (long)big[counter]);
      for(int i=counter-1; i>=0; i--) printf("%.9lu", (long)big[i]);
    }

    putchar('\n');

    return 0;
}
