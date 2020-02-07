#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

void ordered()
{
    printf("Creating 2 child processes --> Controlled\n");

    pid_t pid;
    pid_t pid2;
    int status;
    int status2;

    int max = 1000;

    if((pid = fork()) == 0)
    {
        for (int i = 0; i < max; i++)
        {
            printf("I am CHILD: %d ---- %d\n", getpid(), i);
        }
    }
    else
    {
        waitpid(pid, &status, 0);
        if((pid2 = fork()) == 0)
        {
            for (int i = 0; i < max; i++)
            {
                printf("I am CHILD: %d ---- %d\n", getpid(), i);
            }
            waitpid(pid2, &status2, 0);
        }
    }

    printf("ENDED\n");
}

void unordered()
{
    printf("Creating 2 child processes --> Rage\n");

    pid_t pid;
    pid_t pid2;
    int status;
    int status2;

    int max = 1000;

    if((pid = fork()) == 0)
    {
        for (int i = 0; i < max; i++)
        {
            printf("I am CHILD: %d ---- %d\n", getpid(), i);
        }
        waitpid(pid, &status, 0);
    }
    else
    {
        if((pid2 = fork()) == 0)
        {
            for (int i = 0; i < max; i++)
            {
                printf("I am CHILD: %d ---- %d\n", getpid(), i);
            }
            waitpid(pid2, &status2, 0);
        }
    }

    printf("ENDED\n");
}

int main(int argc, char *argv[])
{
    //ordered();
    unordered();
    return 0;
}