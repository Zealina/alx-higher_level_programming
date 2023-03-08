#include "lists.h"

/**
 * insert_node - insert element into a sorted linked list
 * @head: Pointer to pointer to the head of the list
 * @number, number to insert into the list
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *prev;

	temp == *head;
	while (temp != NULL)
	{
		if (temp->n > number)
		{


		temp = temp->next;
