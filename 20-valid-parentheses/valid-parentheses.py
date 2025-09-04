class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for i in s:
            if i in mapping:
                stack.append(i)
            else:
                if not stack or mapping[stack.pop()] != i:
                    return False
        return not stack
            
            
        