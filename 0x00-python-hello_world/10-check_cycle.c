#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a list
 * @list: linked list
 *
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list, *tmp2;
	int cnt;

	if (list == NULL)
	{
		return (0);
	}
	while (tmp != NULL)
	{
		tmp2 = list;
		cnt = 0;
		while (tmp2 != NULL)
		{
			if (tmp2 == list)
			{
				cnt++;
			}
			if (cnt > 1)
			{
				return (1);
			}
			tmp2 = tmp2->next;

		}
		tmp = tmp->next;
	}
	return (0);
}
