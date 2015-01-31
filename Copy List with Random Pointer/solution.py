def factory():
    return RandomListNode(0)
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        p = head
        nodesMap = collections.defaultdict(factory)
        nodesMap[None] = None
        while p is not None:
            nodesMap[p].label = p.label
            nodesMap[p].next = nodesMap[p.next]
            nodesMap[p].random = nodesMap[p.random]
            p = p.next
        del nodesMap[None]
        return nodesMap[head]