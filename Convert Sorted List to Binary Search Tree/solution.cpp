class Solution {
public:
    TreeNode *sortedListToBST(ListNode *head) {
        return build(head, NULL);
    }

    TreeNode *build(ListNode *head, ListNode *tail) {
        
        if (!head || head == tail)
            return NULL;

        ListNode* p = head;
        ListNode* q = head;

        while (q != tail && q->next != tail) {
            p = p->next;
            q = q->next->next;
        }

        TreeNode* root = new TreeNode(p->val);

        root->left = build(head, p);
        root->right = build(p->next, tail);

        return root;
    }
};