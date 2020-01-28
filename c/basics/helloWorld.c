
#include <stdio.h>

char test[] = "now what motherfucker";

void lol(char *something)
{
    for(int i = 0; i < 50; i++)
    {
        if (something[i] != 0)
        {
            printf("Letter: %c", something[i]);
            printf("\n");
        }
    }
}

void main(int argc, char *argv[])
{
    char str[50]; // Dejar 50 bytes de espacio
    printf("Por favor introduce algo: ");
    scanf("%s", str);
    printf("\n");
    printf("Enserio, eso? Como quieras \n");
    printf("\n");

    lol(str);
}