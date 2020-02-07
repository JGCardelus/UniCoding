#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    pid_t pid1;
    int status1;

    if((pid1=fork()) == 0)
    {
        printf("Child: %d\nParent: %d\n", getpid(), getppid());
    }
    else
    {
        waitpid(pid1, &status1, 0);
        printf("\n%d\n", status1);
        printf("I am PARENT //// %d\n", getpid());
    }

    return 0;
}