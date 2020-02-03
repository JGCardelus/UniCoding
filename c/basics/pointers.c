#include <stdio.h>

void pointer_assignment()
{
    int *ip; // Create pointer
    int var = 10; // Create var and assign value

    //Assign to pointer location of variable
    ip = &var;

    //Print memory location to verify that both locations match
    printf("Memory loc of var: %x \n", &var);
    printf("Memory loc of *ip: %x \n", ip);

    //Print both values
    printf("Value of var: %i \n", var);
    printf("Value of *ip: %i \n", *ip);
}

void test_memory_location()
{
    int a = 1;
    char b[10];

    printf("Memory location of a: %x \n", &a);
    printf("Memory location of b: %x \n", &b);
}

void main(int argc, char *argv[])
{
    test_memory_location();
    pointer_assignment();

    return 0;
}