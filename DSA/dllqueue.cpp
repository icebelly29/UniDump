#include <stdio.h>
#include <stdlib.h>

struct Node {
	int data;
	int priority;
	struct Node *prev, *next;
};

void push(struct Node** fr, struct Node** rr, int n, int p)
{
	struct Node* news = (struct Node*)malloc(sizeof(struct Node*));
	news->data = n;
	news->priority = p;

	if (*fr == NULL) {
		*fr = news;
		*rr = news;
		news->next = NULL;
	}
	else {
		if (p <= (*fr)->priority) {
			news->next = *fr;
			(*fr)->prev = news->next;
			*fr = news;
		}

		else if (p > (*rr)->priority) {
			news->next = NULL;
			(*rr)->next = news;
			news->prev = (*rr)->next;
			*rr = news;
		}

		
		else {
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


int peek(struct Node* fr) { 
	return fr->data; 
}

int isEmpty(struct Node* fr) {
	 return (fr == NULL); 
}

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


void main()
{
    int choice,item1,item2;

	struct Node *front = NULL, *rear = NULL;
	do
    {
        printf("1.Append List\n2.Traverse\n3.Delete\n4.Exit\nEnter your choice?");
        scanf("%d",&choice);
        int temp=*rear;
        switch(choice)
        {
            case 1:
            printf("Enter two numbers");
	    scanf("%d",&item1);
	    scanf("%d",&item2);
            push(&front,&rear,item1,item2);
            case 2:
            for(int i=0;i<=(temp);i++)
	    {
		printf("%d", peek(i));
	     }
	     case 3:
	     pop(&front, &rear);
	     case 4:
	     exit(0);  
             break; 
	     default:
	     printf("\nPlease enter valid choice");
        }
    }
    while(choice != 4);
}
