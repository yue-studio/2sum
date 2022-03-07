#include <stdlib.h>
#include <stdio.h>

typedef struct ListNode {
    int val;
    struct ListNode *next;
} ListNode;

ListNode *newNode(int data) {
    ListNode *newNode = malloc(sizeof(ListNode));
    newNode->val = data;
    newNode->next = NULL;
    return newNode;
}

void printNode(ListNode* l) {
    ListNode *last;
    last = l;
    while (last) {
         printf("%d ", last->val);
         last = last->next;
    }
    printf("\n");
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    ListNode *first, *last, *node, *re;
    int div;
 
    first = newNode(0);
    last = first;

    div = 0;
    while (l1 || l2 || div){
        int sum = div;
        if (l1){
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2){
            sum += l2->val;
            l2 = l2->next;
        }
        div = sum /10;
        node = newNode(sum % 10);
        last->next = node;
        last = node;
    }
    last->next = NULL;
    if (first == last){
        first->val = 0;
        return first;
    }else{
        re = first->next;
        free(first);
        return re;
    }
}

int main() {
    ListNode *a, *b, *c;
    a = newNode(2);
    a->next = newNode(2);
    
    b = newNode(9);
    b->next = newNode(8);
    
    c = addTwoNumbers(a, b);
    printNode(c);
    
    return 0;
}
