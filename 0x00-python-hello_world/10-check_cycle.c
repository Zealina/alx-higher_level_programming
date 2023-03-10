#include "lists.h"
/**
 * freeptr - free the list i created
 * @head: Pointer to the head of the list
 *
 * Return: void
 */
void freeptr(listp_t *head)
{
	listp_t *temp;

	while (head)
	{
		temp = head->next;
		free(head->ptr);
		free(head);
		head = temp;
	}
}
/**
 * check_cycle - Checks if the linked list contains a cycle
 * @list: Pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	listp_t *new, *headptr, *tempptr;

	temp = list;
	headptr = NULL;
	while (temp)
	{
		new = malloc(sizeof(listp_t));
		if (new == NULL)
			exit(98);
		new->ptr = temp;
		new->next = headptr;
		headptr = new;
		tempptr = headptr;
		while (tempptr->next != NULL)
		{
			tempptr = tempptr->next;
			if (tempptr->ptr == temp)
				return (1);
		}
	}
	freeptr(headptr);
	return (0);
}
