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
	if (pos == NULL)
	{
		*head = new;
		return (*head);
	}
	while (pos)
	{
		if (number < pos->next->n || pos->next == NULL)
		{
			new->next = pos->next;
			pos->next = new;
			return (new);
		}
		pos = pos->next;
	}
	return (NULL);
}
