/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 class Solution {
 public:
    ListNode* Merge(ListNode *first, ListNode *second) {
        ListNode *head = new ListNode(-1);
        ListNode *cur = head;
        while (first != NULL || second != NULL) {
            int a = first == NULL ? INT_MAX : first->val;
            int b = second == NULL ? INT_MAX : second->val;
            if (a <= b) {
                cur->next = first;
                first = first->next;
            } else {
                cur->next = second;
                second = second->next;
            }
            cur = cur->next;
        }
        cur = head->next;
        delete head;
        return cur;
    }
    ListNode* mergeSort(ListNode **head, int length) {
        if (length == 1) {
            ListNode *temp = *head;
            *head = (*head)->next;
            temp->next = NULL;
            return temp;
        }
        ListNode *left = mergeSort(head, length / 2);
        ListNode *right = mergeSort(head, length - length / 2);
        ListNode *newHead = Merge(left, right);
        return newHead;
    }
    ListNode* sortList(ListNode *head) {
        if (head == NULL)
            return NULL;
        int len = 0;
        ListNode *p = head;
        while (p != NULL) {
            p = p->next;
            len++;
        }
        ListNode *newHead = mergeSort(&head, len);
        return newHead;
    }
};