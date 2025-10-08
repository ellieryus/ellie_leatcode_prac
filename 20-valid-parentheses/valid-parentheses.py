class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # mapping = {")": "(", "}": "{", "]": "["}
        # stack = []
        # for char in s:
        #     if char in mapping:
        #         top_element = stack.pop() if stack else '#'
        #         if mapping[char] != top_element:
        #             return False
        #     else:
        #         stack.append(char)
        # return not stack    

        mapping = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in mapping:
                stack.append(mapping[char])  
            elif not stack or stack.pop() != char:
                return False
        return not stack

