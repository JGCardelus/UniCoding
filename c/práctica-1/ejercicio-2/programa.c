#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void save_pid(char file_name[])
{
    FILE *pid_file = fopen(file_name, "w");

    int pid = get_child();
    fprintf(pid_file, "PID: %d\n", pid);
    pclose(pid_file);

    printf("File %s saved.", file_name);
}

int get_child()
{
    int child = getpid();
    return child;
}

int get_parent()
{
    int parent = getppid();
    return parent;
}

void print_pids()
{
    int child = get_child();
    int parent = get_parent();
    printf("PID Child: %d\n", child);
    printf("PID Parent: %d\n", parent);
}

int main(int argc, char *argv[])
{
    for (int i = 1; i < argc; i++)
    {
        char *option = argv[i];
        printf("%s\n", option);
        if (strcmp(option, "1") == 0)
        {
            if (argc == 3)
            {
                save_pid(argv[i + 1]);
                break;
            }
            else
            {
                printf("Please provide the name of the file where you want the PID saved.\n");
            }
        }
        else if(strcmp(option,"2") == 0)
        {
            print_pids();
        }
        else
        {
            printf("Option not reconised, please try again.\n");
        }
    }

    printf("Exiting program.\n");
    return 0;
}