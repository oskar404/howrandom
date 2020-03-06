#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define RAND_SIZE 128
#define MAX_BYTE 256
#define MAX_CHAR (1 + 'Z' - 'A')


void store(void* buffer, const char* name)
{
    FILE* fp = fopen(name, "wb");
    if(!fp) {
        perror(name);
        exit(1);
    }
    fwrite(buffer, 1, RAND_SIZE, fp);
    fclose(fp);
}


void create_rand_bytes()
{
    unsigned char buffer[RAND_SIZE];
    memset(buffer, 0, RAND_SIZE);

    srand(1);   /* Set seed to 1 */

    printf("bytes: [");
    for (int i = 0; i < RAND_SIZE; ++i) {
        int value = rand() % MAX_BYTE;
        printf("%s%d",  (i > 0 ? " ," : ""), value);
        buffer[i] = (unsigned char)(value);
    }
    printf("]\n");
    store(buffer, "rand.bin");
}


void create_rand_chars()
{
    char buffer[RAND_SIZE];

    srand(1);   /* Set seed to 1 */

    printf("string: ");
    for (int i = 0; i < RAND_SIZE; ++i) {
        buffer[i] = 'A' + rand() % MAX_CHAR;
        printf("%c", buffer[i]);
    }
    printf("\n");
    store(buffer, "rand.txt");
}


int main()
{
    create_rand_bytes();
    create_rand_chars();
    return 0;
}
