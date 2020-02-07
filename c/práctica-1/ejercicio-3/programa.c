#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int PID;
    FILE *file;
    char pid[5];

    system("firefox &"); // Ejecuta este comando en la consola, que activa firefox
    system("pidof -s firefox > /tmp/pid-of-firefox"); // Imprime el pid de firefox en el archivo
    // pid-of-firefox en la carpeta tmp
    file = fopen("/tmp/pid-of-firefox", "rb"); // Abre el arhivo en modo read-bytes
    fread(pid, sizeof(pid), 1, file); // Lee de file un conjunto de bytes the tamaño de pid_t y lo guarda en PID

    printf("\nProceso padre: %d\nProceso actual %d\nProceso firefox: %s\n\nFin del programa\n", getppid(), getpid(), pid);
    return 0;
}