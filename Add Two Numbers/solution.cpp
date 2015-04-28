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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    	int carry = 0;
    
    	ListNode* p = l1;
    	ListNode* q = l2;
    
    	ListNode* ans = new ListNode(0);
    	ListNode* head = ans;
    
    	while (p && q) {
    		head->next = new ListNode(0);
    		head = head->next;
    		head->val = (p->val + q->val + carry) % 10;
    		carry = (p->val + q->val + carry) / 10;
    		p = p->next;
    		q = q->next;
    	}
    
    	while (p) {
    		head->next = new ListNode(0);
    		head = head->next;
    		head->val = (p->val + carry) % 10;
    		carry = (p->val + carry) / 10;
    		p = p->next;
    	}
    
    	while (q) {
    		head->next = new ListNode(0);
    		head = head->next;
    		head->val = (q->val + carry) % 10;
    		carry = (q->val + carry) / 10;
    		q = q->next;
    	}
    
        if (carry > 0) {
            head->next = new ListNode(0);
            head = head->next;
            head->val = carry;
        }
        
    	return ans->next;
    }
};