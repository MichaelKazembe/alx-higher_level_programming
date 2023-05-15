#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return 1;

	listint_t *slow = *head;
	listint_t *fast = *head;
    	listint_t *prev = NULL;
    	listint_t *second_half = NULL;
    	listint_t *mid_node = NULL;
    	int is_palindrome = 1;


   	while (fast != NULL && fast->next != NULL)
      	{
      		fast = fast->next->next;
      		prev = slow;
      		slow = slow->next;
      	}

    	if (fast != NULL)
    	{
        	mid_node = slow;
        	slow = slow->next;
    	}

    	second_half = reverse_list(slow);

    	listint_t *p1 = *head;
    	listint_t *p2 = second_half;
    	while (p2 != NULL)
    	{
        	if (p1->n != p2->n)
        	{
            	is_palindrome = 0;
            	break;
     	}
      	p1 = p1->next;
      	p2 = p2->next;
    	}

    	reverse_list(second_half);

    	if (prev != NULL)
        	prev->next = second_half;
    	else
        	*head = second_half;

    	if (mid_node != NULL)
        	mid_node->next = slow;

    	return is_palindrome;
	}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 * Return: pointer to the new head of the reversed list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
      	listint_t *curr = head;
      	listint_t *next = NULL;

      	while (curr != NULL)
      	{
      		next = curr->next;
        	curr->next = prev;
        	prev = curr;
        	curr = next;
    	}

    	return prev;
}

