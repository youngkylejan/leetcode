class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if start == end:
            return 2
        queue = collections.deque()
        queue.append(start)
        maps = {}
        maps[start] = 0
        l = len(end)
        flag = {}
        for item in dict:
            flag[item] = 0
        flag[start] = 1
        while len(queue) > 0:
            if 0 not in flag.values():
                break
            front = queue.popleft()
            chars = list(front)
            for i in range(0, l):
                head = ''.join(chars[0:i])
                tail = ''.join(chars[i+1:l])
                for j in range(ord('a'), ord('z') + 1):
                    next = head + chr(j) + tail
                    if next in dict and flag[next] == 0:
                        flag[next] = 1
                        maps[next] = maps[front] + 1
                        queue.append(next)
                        if next == end:
                            return maps[next] + 1
        return 0