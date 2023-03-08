#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert element into a sorted linked list
 * @head: Pointer to pointer to the head of the list
 * @number: number to insert into the list
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	temp = *head;
	while (temp != NULL)
	{
		if (temp->n > number)
		{
			new->next = temp;
			prev->next = new;
			return (new);
		}
		prev = temp;
		temp = temp->next;
	}
	temp->next = new;
	return (new);
}
