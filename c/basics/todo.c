#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Item
{   
    // Item information
    char *task;
    char *description;
    int priority;
    int is_completed;
    // Array information
    struct Item *next;
} item;

typedef struct Array
{
    int len;
    item *start;
    item *end;
} array;

array todo = {
    0,
    NULL,
    NULL
};

// This function takes in the array object and a number
// Could be rewritten as isert in last position, but this is faster as it uses "end"
void append(array *_array, item *new_item)
{
    // Modify array
    _array->len++;

    // If start of array is null, set this item as the start of the array
    if (_array->start == NULL)
    {
        _array->start = new_item;
    }

    // If end of array is null, set this item as the end of the array
    if (_array->end == NULL)
    {
        _array->end = new_item;
    }
    else
    {
        /* 
        If it is not the&test last element of the array, update the next pointer of the
        last element of the array 
        */
        item *last_elem = _array->end;
        last_elem->next = new_item;
        _array->end = new_item;
    }
}

// Insert element in i position
void insert(array *_array, int n, item *new_item)
{
    if (n >= _array->len)
    {
        // If the user wants to append an item use append() wich is much faster
        append(_array, new_item);
    }
    else
    {
        // Iterate through elements in list until element[i] is found
        item *elem = _array->start;
        int counter = 1; // Start at 1 because elem is already position 0
        while (counter < n)
        {
            elem = elem->next;
            counter++;
        }

        // Update pointers
        item *old_next = elem->next;
        elem->next = new_item; // Element in position (i - 1) goes to new_item
        new_item->next = old_next; // New item next's goes to previous i item

        _array->len++;
    }
}

item * get(array *_array, int n)
{
    int counter = 0;
    item *iteration = _array->start;

    while (counter < n)
    {
        // Get the next element in the array
        iteration = iteration->next;
        counter++;
    }
    // Return the pointer that contains the element required by the user
    return iteration;
}

item * new(char *task, char *description)
{
    item *new_item;
    new_item = (item *) malloc (sizeof(item));

    new_item->task = (char *)malloc(strlen(task) + 1);
    strcpy(new_item->task, task);

    new_item->description = (char *)malloc(strlen(description) + 1);
    strcpy(new_item->description, description);

    new_item->next = NULL;

    return new_item;
}

void delete(array *_array, int n)
{
    item *start = _array->start;
    int last = (_array->len - 1);
    // Initial checks
    if (n >= _array->len || n < 0)
    {
        printf("Index out bounds exception: The element requested is not in the array\n");
    }

    if (n == 0)
    {
        // If the item to delete == 0, the start element is now the second element
        item *new_start = get(_array, 1);
        _array->start = new_start;
    }
    else if (n == last)
    {
        item *new_last = get(_array, last - 1);
        _array->end = new_last;
    }
    else
    {
        item *a = get(_array, n - 1);
        // Get element previous to the one to delete
        // Get element next to the one to delete
        item *b = (a->next)->next;
        // Join a and b
        a->next = b;
    }  

    // Update array len
    _array->len--;
}

void pop(array *_array)
{
    delete(_array, (_array->len - 1));
}

void shift(array *_array)
{
    delete(_array, 0);
}

void show_tasks()
{
    printf("\nItems in todo list: \n");
    for (int i = 0; i < todo.len; i++)
    {
        item *elem = get(&todo, i);
        printf("%i: ", i);
        printf("%s", elem->task);
    }
}

item *guided_new_task()
{
    printf("\nNew task: \n");
    // fgets does not work properly, this solves the issue
    char dummy[5];
    fgets(dummy, 6, stdin);

    // Actual program
    char task[128];
    printf("    Task > ");
    fgets(task, 128, stdin);

    char description[128];
    printf("    Description > ");
    fgets(description, 129, stdin);

    item *new_task = new(task, description);
}

int add_task()
{
    item *new_task = guided_new_task();
    append(&todo, new_task);

    return 0;
}

int insert_task()
{
    item *new_task = guided_new_task();

    while (1)
    {
        printf("    Position to insert in [0, %d]> ", todo.len - 1);
        int index;
        scanf("%d", &index);
        printf("\n");

        if (index <= todo.len && index >= 0)
        {
            insert(&todo, index, new_task);
            break;
        }
        else
        {
            printf("Invalid number. The number must be inserted between 0 and %d\n", todo.len -1);
        }
    }

    return 0;
}

int show_all()
{
    if (todo.len == 0)
    {
        printf("There are no tasks available.\n");
    }
    else
    {
        printf("Tasks: \n\n");
        for(int i = 0; i < todo.len; i++)
        {
            item *task = get(&todo, i);
            printf("    %d: %s", i, task->task);
        }
        printf("\n");   
    }

    return 0;
}

int delete_task()
{
    printf("\nDelete task: \n\n");
    if (todo.len >= 1)
    {
        show_all();
        while(1)
        {
            printf("    Element to delete [0, %d], insert -1 to cancel operation > ", todo.len -1);
            int index;
            scanf("%d", &index);
            printf("\n");
            if (index < todo.len && index >= 0)
            {
                delete(&todo, index);
                break;
            }
            else
            {
                if (index == -1)
                {
                    printf("Operation cancelled.\n");
                }
                else
                {
                    printf("Invalid number. The number must be inserted between 0 and %d\n", todo.len -1);
                }
            }
            
        }
    }
    else
    {
        printf("There are no tasks available. \n");
    }
    return 0;
    
}

int delete_last_task()
{
    int option;
    printf("\nDelete last task. \n\n");
    if (todo.len >= 1)
    {
        while (1)
        {
            printf("    Are you sure you want to proceed [>= 0, yes // <= -1, no] > ");
            scanf("%d", &option);
            if (option >= 0)
            {
                pop(&todo);
                printf("Deleted\n");
                break;
            }
            else if(option <= -1)
            {
                printf("Operation cancelled.\n");
            }
        }
    }
    else
    {
        printf("There are no tasks available. \n");
    }

    return 0;
}

int delete_first_task()
{
    int option;
    printf("\nDelete first task. \n\n");
    if (todo.len >= 1)
    {
        while (1)
        {
            printf("    Are you sure you want to proceed [>= 0, yes // <= -1, no] > ");
            scanf("%d", &option);
            if (option >= 0)
            {
                shift(&todo);
                printf("Deleted\n");
                break;
            }
            else if(option <= -1)
            {
                printf("Operation cancelled.\n");
            }
        }
    }
    else
    {
        printf("There are no tasks available. \n");
    }

    return 0;
}

int expand_task()
{
    if (todo.len >= 1)
    {
        show_all();
        printf("\nExpand task \n\n");
        while(1)
        {
            printf("    Element to expand [0, %d], insert -1 to cancel operation > ", todo.len -1);
            int index;
            scanf("%d", &index);
            printf("\n");
            if (index < todo.len && index >= 0)
            {
                item *task = get(&todo, index);
                printf("\n\n*******************************\n%s*******************************\n\n", task->task);
                printf("%s\n", task->description);
                printf("    --> Task nº: %d\n\n", index);
                break;
            }
            else
            {
                if (index == -1)
                {
                    printf("Operation cancelled.\n");
                }
                else
                {
                    printf("Invalid number. The number must be inserted between 0 and %d\n", todo.len -1);
                }
            }
            
        }
    }
    else
    {
        printf("There are no tasks available.\n");
    }
    
    return 0;
}

int menu()
{
    printf("***********************************+*\n");
    printf("\n              MENU\n");
    printf("\n***********************************+*\n");
    printf("\n");
    printf("\nPlease select one of the following: \n");
    printf(" // Maintenance:\n");
    printf("    1 -> Add task\n");
    printf("    2 -> Insert task\n");
    printf("    3 -> Delete task\n");
    printf("    4 -> Delete last task\n");
    printf("    5 -> Delete first task\n");
    printf(" // Information\n");
    printf("    6 -> Show all tasks\n");
    printf("    7 -> Expand task\n");
    printf(" // Quit\n");
    printf("    8 -> Quit\n");
    printf("\n\n");
    
    int option;
    printf("    >>> ");
    scanf("%d", &option);

    int status;
    switch (option)
    {
        case 1:
            status = add_task();
        break;

        case 2:
            status = insert_task();
        break;

        case 3:
            status = delete_task();
        break;

        case 4:
            status = delete_last_task();
        break;

        case 5:
            status = delete_first_task();
        break;

        case 6:
            status = show_all();
        break;

        case 7:
            status = expand_task();
        break;

        case 8:
            status = 1;
        break;
    }

    if (status == 1)
    {
        return 0;
    }

    return 1;
}

void intro()
{
    printf("***********************************+********************\n");
    printf("\nWelcome to Jorge's infinite (or until the ram runs out :)) todo list\n");
    printf("\n***********************************+********************\n");
    printf("\n");

    printf("The program is based on a system that can create arrays of infinte length with the use of pointers.\n");
    printf("The functions built in the system are:\n");
    printf("    append(*_array, *new_item): Adds an item to the last element of the list.\n");
    printf("    insert(*_array, n, *new_item): Inserts element in the n-th position of the list.\n");
    printf("    get(*_array, n): Gets the n-th element on the list.\n");
    printf("    new(*task, *description): Creates a 'item' struct, fills task and description, and then returns it.\n");
    printf("    delete(*_array, n): Deletes the n-th item on the list.\n");
    printf("    pop(*_array): Deletes the last item.\n");
    printf("    shift(*_array): Deletes the first item. \n");
    printf("\n");
    printf("If you want to call a function you must pass as *_array the pointer of an 'array' struct. In this case we are working with 'todo'.\n");
    printf("For example, if you want to create a new item and append it to the todo array: \n");
    printf("    char task[50] = 'Do laundry';\n");
    printf("    char description[200] = 'Take laundry out of the washing machine';\n");
    printf("    item *task = new(&task, &description);\n");
    printf("    append(&todo, task);\n");
    printf("\n");
    printf("The append function is specially efficient as it can add a new item with 1 operation and accessing memory 5 times.\n");
    printf("The rest of operations have a maximum of n operations to complete their task -> O(g(x)) = n\n");

    printf("\nIf you do not wish to try the functions in the source code, the operations can be observed using the program through the command line.\n");
    printf("Enjoy.\n");
}

void main(int argc, char *argv[]) //No need for return
{
    intro();
    int state = 1;
    while (state == 1)
    {
        state = menu();
    }
    printf("Thank you for using Jorge's infinite (or until the ram runs out, whatever comes first :)) todo list.\nSee you soon!\n");
}