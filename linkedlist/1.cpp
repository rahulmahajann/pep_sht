#include<bits/stdc++.h>
using namespace std;

class node{
    public:
        int data;
        node* next;       
};

int main(){
    node* d;
    node* head=NULL;
    
    for(int i=0;i<5;i++){
        node* newNode = new node;
        newNode->data = i+1;
        if(head == NULL){
            head = newNode;
            d = head;
        }else{
            head->next = newNode;
            head = newNode; 
        }
        newNode->next = NULL;
    }

    node* midnode= new node;
    midnode->data=20;
    midnode->next=d;
    d=midnode;

    head = d;
    while(head != NULL){
        cout<<head->data<<" ";
        head = head->next;
    }

    return 0;
}