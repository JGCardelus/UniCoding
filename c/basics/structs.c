#include<stdio.h>

struct Person
{
    char name[50];
    char surname_a[50];
    char surname_b[50];
    int age;
};

void print_data(struct Person person)
{
    printf("Name: %s\n", person.name);
    printf("First surname: %s\n", person.surname_a);
    printf("Second surname: %s\n", person.surname_b);
    printf("Age: %i\n", person.age);
}

void main(int argc, char *argv[])
{
    struct Person jorge = {
        "Jorge",
        "González",
        "Cardelús",
        18
    };

    print_data(jorge);

}