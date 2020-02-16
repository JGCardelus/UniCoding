#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    char comando[100] = "gedit ";
    strcat(comando, argv[1]);
    system(comando);

    return 0;
}