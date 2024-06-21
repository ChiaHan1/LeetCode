/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // the size of the linkedlist
    int size = 0;

    struct ListNode* current = head;
    
    while (current != NULL) {
        size++;
        current = current->next;
    }

    current = head;

    if (size == n) {
        return head->next;
    }

    for (int i = 0; i < size - n - 1; i++) {
        current = current->next;
    }

    struct ListNode* removed = current->next;
    current->next = current->next->next;
    // free(removed);

    return head;
}