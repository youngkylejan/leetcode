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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        ListNode **p = &head, *q = head;
        for (int i = 1; i < n; i++) {
            q = q->next;
        }
        while (q->next) {
            p = &((*p)->next);
            q = q->next;
        }
        *p = (*p)->next;
        return head;
    }
};