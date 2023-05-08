#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - Program for singly linked list
 * @n: number
 * @next: refers to the next node in the list
 * Description: singly linst node project
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);








#endif /* LISTS_H */
