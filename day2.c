#include <stdio.h>
#include <string.h>

int main(void)
{
    FILE* f = fopen("input2.txt", "r");
    int ok = 1;
    int matches1 = 0;
    int matches2 = 0;
    while(1) {
        unsigned int min, max;
        char c;
        char buffer[256];
        ok = fscanf(f, "%u-%u %c: %s", &min, &max, &c, (char*)buffer);
        if (ok == 4) {
            int count = 0;
            int len = strlen(buffer);
            for(int i=0; i<len; i++) {
                if(buffer[i] == c) {
                    count += 1;
                }
            }
            if(count <= max && count >= min) {
                matches1++;
            }
            if((max <= len) && (min <= len) &&
               (buffer[min-1] == c) ^ (buffer[max-1] == c)) {
                matches2++;
            }
        } else {
            break;
        }
    }
    fclose(f);
    printf("%d\n%d\n", matches1, matches2);
    return 0;
}
