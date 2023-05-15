#include "lists.h"
#include <stddef.h>

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Program reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp = NULL;

	while (fast != NULL && fast->next != NULL)
	{
	fast = fast->next->next;
	temp = slow;
	slow = slow->next;
	temp->next = prev;
	prev = temp;
	}

	if (fast != NULL)
	{
	slow = slow->next;
	}

	while (slow != NULL && prev != NULL)
	{
	if (slow->n != prev->n)
	{
		return (0);
	}
	slow = slow->next;
	prev = prev->next;
	}

	return (1);
}
