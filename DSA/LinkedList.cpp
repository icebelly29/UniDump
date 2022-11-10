#include <bits/stdc++.h>
#include <iostream>
using namespace std;
class Node {
    public:
    int data;
    Node* next;
};

int main() 
{
    Node* head;
    Node* first = NULL;
    Node* second = NULL;
    Node* third= NULL;
    first = new Node();
    second= new Node();
    third = new Node();
    first->data=1;
    first->next=second;
    
    second->data=2;
    second->next=third;
    
    third->data=3;
    third->next=NULL;
    head=first;
    while(head!=NULL)
    {
        cout <<head->data;
        head=head->next;
    }
    
    return 0;
}       
