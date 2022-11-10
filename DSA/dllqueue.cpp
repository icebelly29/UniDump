// C code to implement priority
// queue using doubly linked list
#include <stdio.h>
#include <stdlib.h>

// Linked List Node
struct Node {
	int data;
	int priority;
	struct Node *prev, *next;
};

// Function to insert a new Node
void push(struct Node** fr, struct Node** rr, int n, int p)
{
	struct Node* news
		= (struct Node*)malloc(sizeof(struct Node*));
	news->data = n;
	news->priority = p;

	// If linked list is empty
	if (*fr == NULL) {
		*fr = news;
		*rr = news;
		news->next = NULL;
	}
	else {
		// If p is less than or equal front
		// node's priority, then insert at
		// the front.
		if (p <= (*fr)->priority) {
			news->next = *fr;
			(*fr)->prev = news->next;
			*fr = news;
		}

		// If p is more rear node's priority,
		// then insert after the rear.
		else if (p > (*rr)->priority) {
			news->next = NULL;
			(*rr)->next = news;
			news->prev = (*rr)->next;
			*rr = news;
		}

		// Handle other cases
		else {

			// Find position where we need to
			// insert.
			struct Node* start = (*fr)->next;
			while (start->priority > p)
				start = start->next;
			(start->prev)->next = news;
			news->next = start->prev;
			news->prev = (start->prev)->next;
			start->prev = news->next;
		}
	}
}

// Return the value at rear
int peek(struct Node* fr) { return fr->data; }

int isEmpty(struct Node* fr) { return (fr == NULL); }

// Removes the element with the
// least priority value from the list
int pop(struct Node** fr, struct Node** rr)
{
	struct Node* temp = *fr;
	int res = temp->data;
	(*fr) = (*fr)->next;
	free(temp);
	if (*fr == NULL)
		*rr = NULL;
	return res;
}


int main()
{
    int choice,item1,item2;

	struct Node *front = NULL, *rear = NULL;
	push(&front, &rear, 2, 3);
	push(&front, &rear, 3, 4);
	push(&front, &rear, 4, 5);
	push(&front, &rear, 5, 6);
	push(&front, &rear, 6, 7);
	push(&front, &rear, 1, 2);
	do
    {
        cout<<"1.Append List\n2.Traverse\n3.Delete\n4.Exit\nEnter your choice?"<<;
        cin>>&choice>>;
        switch(choice)
        {
            case 1:
            cout<<"Enter two number"<<;
            cin>>&item>>;
            push(&front,&rear,&item1,&item2);
            case 2:
            
        }
    }

	printf("%d\n", pop(&front, &rear));
	printf("%d\n", peek(front));
	return 0;
}
