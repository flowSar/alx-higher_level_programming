#include "lists.h"
/**
 * check_cycle - this function to check if there's a cycle in linkedlist.
 * @list: linkedlist head.
 * Return: return 1 if cycle found and 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *prev = list;
	listint_t *tmp = list;

	while (prev)
	{
		if (prev->next == tmp)
			return (1);
		prev = prev->next;
	}

	return (0);
}
