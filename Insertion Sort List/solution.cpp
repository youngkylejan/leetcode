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
    ListNode* insertionSortList(ListNode* head) {
        if (!head)
            return NULL;

        ListNode* tmp = new ListNode(0);
        tmp->next = head;

        ListNode* p = head;

        while (p->next) {
            if (p->next->val < p->val) {
                ListNode* pre = tmp;
                
                while (pre->next->val < p->next->val)
                    pre = pre->next;

                ListNode* tail = p->next->next;
                p->next->next = pre->next;
                pre->next = p->next;
                p->next = tail;
            } else {
                p = p->next;
            }
        }

        return tmp->next;
    }
};