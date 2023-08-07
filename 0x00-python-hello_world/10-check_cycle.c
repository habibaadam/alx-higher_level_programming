#include "lists.h"

/**
 * check_cycle - checks whether a linked list has a cycle or not
 * @list: the linked list
 * Return: 1 if there is a cycle and 0 if otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *calm = list;
	listint_t *quick = list;

	/* cycle not present */
	if (!list)
		return (0);

	while (quick && calm && quick->next)
	{
		calm = calm->next;
		quick = quick->next->next;

		/* if a cycle is found */
		if (calm == quick)
		{
			return (1);
		}
	}
	return (0);
}

