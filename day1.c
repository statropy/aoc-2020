//day1.c
#include <stdio.h>
#include <inttypes.h>
#include <string.h>

static uint64_t bitfields[32];

#define INDEX(a)    (a >> 6)
#define BIT(a)      (((uint64_t)1) << (a & 0x3F))
#define TEST(a)     (bitfields[INDEX(a)]  & BIT(a)) 
#define SET(a)      (bitfields[INDEX(a)] |= BIT(a))
#define RESET()     (memset(bitfields, 0, sizeof(bitfields)))
#define NEXT(a)     (fscanf(f, "%llu", &a) == 1)

uint64_t part1(void)
{
    uint64_t amount, match;
    FILE *f = fopen("input1.txt", "r");

    RESET();

    while(NEXT(amount)) {
        match = 2020 - amount;
        if(TEST(match)) {
            break;
        }
        SET(amount);
    }
    fclose(f);
    return amount*match;
}

uint64_t part2(void)
{
    uint64_t amount, match, second;
    FILE *f = fopen("input1.txt", "r");

    RESET();

    while(NEXT(amount)) {
        
        rewind(f);
        NEXT(second);

        while(second != amount) {
            if(amount + second <= 2020) {
                match = 2020 - amount - second;
                if(TEST(match)) {
                    fclose(f);
                    return amount*match*second;
                }
            }
            NEXT(second);
        }
        SET(amount);
    }
    fclose(f);
    return 0;
}

int main(void)
{
    printf("%llu\n", part1());
    printf("%llu\n", part2());
}
