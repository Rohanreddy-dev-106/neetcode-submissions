class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
        "]": "[", 
        "}": "{", 
        ")": "("}

        for i in s:
            if i in "[({":
                stack.append(i)
            else:
                
                if len(stack)!=0 and stack[-1] == hashmap[i]:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0