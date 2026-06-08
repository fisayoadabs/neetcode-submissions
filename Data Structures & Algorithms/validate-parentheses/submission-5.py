class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        closed ={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for i in s:
            if i in closed:
                if not stack:
                    return False
                top = stack.pop()
                if closed[i] != top:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0