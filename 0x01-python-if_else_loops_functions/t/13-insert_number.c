#include "lists.h"

/**
 * insert_node - adds a new node in a sorted list
 * @head: head of the linked list
 * @number: data to be added
 *
 * Return: returns the address of the new node or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new;

	tmp = *head;
	if (head == NULL || *head == NULL)
	{
		return (NULL);
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	while (tmp->next != NULL)
	{
		if (tmp->next->n >= number)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
