#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: Pointer to start of linked list
 * @number: value for new node
 * Return: address of the new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pos = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while (pos)
	{
		if (number > pos->n && number < pos->next->n)
		{
			new->next = pos->next;
			pos->next = new;
		}
		pos = pos->next;
	}
	return (new);
}
