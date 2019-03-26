def is_wellBalanced(s):
    stack = []

    for x in s:
        if x == '(' or x == '[' or x == '{':
            stack.append(x)

        elif x == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return False
            stack.pop()
        elif x == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
        elif x == '}':
            if len(stack) == 0 or stack[-1] != '{':
                return False
            stack.pop()

    return len(stack) == 0


s = '{({})}}}}}}'
print is_wellBalanced(s)
s = '()'
print is_wellBalanced(s)
