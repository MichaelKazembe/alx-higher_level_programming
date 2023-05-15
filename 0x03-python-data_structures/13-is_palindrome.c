#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - reverses singly-linked list.
 * @head: pointer to starting node of the list to reverse
 * Return: pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head;
 	listint_t *next;
      listint_t *previous = NULL;

	while (node)
	{
		next = node->next;
		node->next = previous;
		previous = node;
		node = next;
	}

	*head = previous;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: 0 if list is Palindrome. -1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
 	listint_t *reverse;
	listint_t *mid;
	size_t i;
 	size_t size = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
	{
		temp = temp->next;
	}

	if ((size % 2) == 0 && temp->n != temp->next->n)
	{
		return (0);
	}

	temp = temp->next->next;
	reverse = reverse_listint(&temp);
	mid = reverse;

	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
		{
			return (0);
		}
		temp = temp->next;
		reverse = reverse->next;
	}
	reverse_listint(&mid);

	return (1);
}
