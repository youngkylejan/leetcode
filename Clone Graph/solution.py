# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        nodesMap = {node.label : UndirectedGraphNode(node.label)}
        self.BFSClone(node, nodesMap)
        return nodesMap[node.label]
    def BFSClone(self, node, nodesMap):
        queue = collections.deque()
        queue.append(node)
        newQueue = collections.deque()
        newQueue.append(nodesMap[node.label])
        visited = set([node.label])
        while len(queue) > 0:
            frontOld = queue.popleft()
            frontNew = newQueue.popleft()
            for item in frontOld.neighbors:
                if item.label not in nodesMap:
                    nodesMap[item.label] = UndirectedGraphNode(item.label)
                                frontNew.neighbors.append(nodesMap[item.label])
                if item.label not in visited:
                    queue.append(item)
                    newQueue.append(nodesMap[item.label])
                    visited.add(item.label)
        