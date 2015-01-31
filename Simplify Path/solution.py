class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        path = path.split("/")
        i = 0
        while i < len(path):
            if path[i] == "." or path[i] == '':
                i = i + 1
                continue
            if path[i] == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(path[i])
            i = i + 1
        result = ""
        while len(stack) > 0:
            result = "/" + stack.pop() + result
        return result if result != "" else "/"