//day3.c

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int traverse_memory(const char *treemap, long width, long lines, int right, int down)
{
    int x = 0;
    int y = 0;
    int count = 0;
    char (*arr)[width] = (char (*)[width])treemap;

    while(y < lines) {
        if(arr[y][x] == '#') {
            count++;
        }
        x = (x + right) % (width-1);
        y += down;
    }
    return count;
}

int traverse_file(FILE* f, long width, int right, int down)
{
    int x = 0;
    int count = 0;

    rewind(f);

    while(1) {
        int c = fgetc(f);
        if(c == EOF) {
            return count;
        } else if(c == '#') {
            count++;
        }
        fseek(f, width-x-1, SEEK_CUR); // end of line
        x = (x + right) % (width-1); //next offset
        fseek(f, (down-1)*width + x, SEEK_CUR); //next char
    } 

    return count;
}

int main(void)
{
    FILE* f = fopen("input3.txt", "rb");

    while(fgetc(f) != '\n');
    long width = ftell(f);
    fseek(f, -1, SEEK_END);
    int c = fgetc(f);
    long filesize = ftell(f);
    if(c != '\n') {
        filesize++;
    }
    long lines = filesize / width;
    rewind(f);

    char *treemap = malloc(filesize);
    fread(treemap, width, lines, f);
    
    printf("Memory traversal: ");
    long prodm = traverse_memory(treemap, width, lines, 3, 1);
    printf("%ld, ", prodm);

    prodm *= traverse_memory(treemap, width, lines, 1,1);
    prodm *= traverse_memory(treemap, width, lines, 5,1);
    prodm *= traverse_memory(treemap, width, lines, 7,1);
    prodm *= traverse_memory(treemap, width, lines, 1,2);

    printf("%ld\n", prodm);
    free(treemap);

    printf("File traversal:   ");
    long prodf = traverse_file(f, width, 3, 1);
    printf("%ld, ", prodf);

    prodf *= traverse_file(f, width, 1,1);
    prodf *= traverse_file(f, width, 5,1);
    prodf *= traverse_file(f, width, 7,1);
    prodf *= traverse_file(f, width, 1,2);

    printf("%ld\n", prodf);

    fclose(f);

    return 0;
}
