class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False       
            elif s[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

# Example usage:
s = input('Enter your parentheses set: ')
ou = Solution()
out = ou.isValid(s)
print(out)


'''if stack and stack[-1] == '(':
    stack.pop()
does two things:

Check if the Stack is Not Empty (if stack):

if stack checks whether the list stack is not empty.
In Python, an empty list evaluates to False, and a non-empty list evaluates to True.
This part ensures that you don’t try to access stack[-1] if the stack is empty, which would cause an IndexError.
Check the Top Element (stack[-1] == '('):

stack[-1] accesses the top element of the stack (the last element of the list).
This part checks if the top element is '('.
Pop the Top Element (stack.pop()):

stack.pop() removes the top element (last element) from the list.
It’s executed if the conditions above are true, meaning that the stack is not empty and the top element is '('.'''