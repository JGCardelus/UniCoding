#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
    printf("argc: %i \n", argc);
    printf("argv: %s \n", argv);

    while (1)
    {
        char a[1];
        scanf("%s", a);
    }

    return 0;
}