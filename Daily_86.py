# Cost O(n)
# The algorithim is  modification of the algorithim to check if a string is well parethised
# using a stack (if there is only one type a counter can be used)
# There are two situations in which we have to remove a parenthesis (or update a counter).
# One is when we find a closing parenthesis and the stack is empty.
# The second one is when the sequence is finished but there are still elements on the stack.
def elements_to_fix_parenths(s):
    stack = []
    total = 0

    for x in s:
        if x == '(':
            stack.append('(')
        if x == ')':
            if len(stack) == 0:
                total += 1
            else:
                stack.pop()

    return total + len(stack)


s = ')('
print(elements_to_fix_parenths(s))
s = ')(()('
print(elements_to_fix_parenths(s))
s = '()())()'
print(elements_to_fix_parenths(s))
