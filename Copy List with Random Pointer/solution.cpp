
struct RandomListNode {
  int label;
  RandomListNode *next, *random;
  RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
};

class Solution {
public:

    RandomListNode *copyRandomList(RandomListNode *head) {

        unordered_map<RandomListNode*, RandomListNode*> nodesMap;

        RandomListNode* p = head;

        while (p) {
            if (nodesMap.find(p) == nodesMap.end())
                nodesMap[p] = new RandomListNode(0);
            
            nodesMap[p]->label = p->label;

            if (nodesMap.find(p->next) == nodesMap.end() && p->next)
                nodesMap[p->next] = new RandomListNode(0);
            nodesMap[p]->next = nodesMap[p->next];

            if (nodesMap.find(p->random) == nodesMap.end() && p->random)
                nodesMap[p->random] = new RandomListNode(0);

            nodesMap[p]->random = nodesMap[p->random];
            
            p = p->next;
        }

        return nodesMap[head];
    }
};