
struct UndirectedGraphNode {
  int label;
  vector<UndirectedGraphNode *> neighbors;
  UndirectedGraphNode(int x) : label(x) {};
};


class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {

        if (!node)
            return NULL;

        std::unordered_map<int, UndirectedGraphNode*> nodesMap;
        nodesMap[node->label] = new UndirectedGraphNode(node->label);

        std::queue<UndirectedGraphNode*> old_queue;
        std::queue<UndirectedGraphNode*> new_queue;
        std::set<int> visit;

        old_queue.push(node);
        new_queue.push(nodesMap[node->label]);
        visit.insert(node->label);

        while (!old_queue.empty()) {
            
            auto old_front = old_queue.front();
            auto new_front = new_queue.front();

            for (auto neighbor : old_front->neighbors) {
                
                if (nodesMap.find(neighbor->label) == nodesMap.end())
                    nodesMap[neighbor->label] = new UndirectedGraphNode(neighbor->label);
                
                nodesMap[new_front->label]->neighbors.push_back(nodesMap[neighbor->label]);

                if (visit.find(neighbor->label) == visit.end()) {
                    old_queue.push(neighbor);
                    new_queue.push(nodesMap[neighbor->label]);
                    visit.insert(neighbor->label);
                }
            }

            old_queue.pop();
            new_queue.pop();
        }

        return nodesMap[node->label];
    }
};