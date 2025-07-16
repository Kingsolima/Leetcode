class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {"}": "{", ")": "(", "]": "["}
        stack = []
        for character in s:
            if character in pairs.values():
                stack.append(character)
            elif character in pairs:
                if not stack or stack[-1] !=pairs[character]:
                    return False
                stack.pop()
            else:
                return False
        return not stack

