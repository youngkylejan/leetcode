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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *pa = headA, *pb = headB;
        while (pa && pb) {
            pa = pa->next;
            pb = pb->next;
        }
        while (pa) {
            headA = headA->next;
            pa = pa->next;
        }
        while (pb) {
            headB = headB->next;
            pb = pb->next;
        }
        while (headA && headA != headB) {
            headA = headA->next;
            headB = headB->next;
        }
        return headA;
    }
};