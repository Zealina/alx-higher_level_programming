#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;
/**
 * struct listp_s - pointer to elements in singly linked list
 * @ptr: Pointer to the element
 * @next: pointer to the next node
 *
 * Description: Singly linked list node pointers
 *
 */
typedef struct listp_s
{
	listint_t *ptr;
	struct listp_s *next;
} listp_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t **list);
void freeptr(listint_t **head);

#endif /* LISTS_H */
