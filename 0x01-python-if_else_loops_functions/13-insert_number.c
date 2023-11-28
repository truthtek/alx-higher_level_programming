#include <lists.h>

typedef struct Node {
    int data;
    struct Node* next;
} listint_t;

listint_t* insert_node(listint_t** head, int number) {
    // Create a new node
    listint_t* new_node
