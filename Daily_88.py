# Cost is linear the loop is repeated n times being n the quotioent
# In this problem we have to implement division of two positive integers
# without using the division, multiplication, or modulus operators.
# We are using the subtraction, If we subtract the dividend from the divisor until
# the dividend beccomes greater the number of times we do this is the quotient
def div(a, b):
    res = 0

    while a >= b:
        res += 1
        a -= b

    return res, a


print(div(24, 2))
print(div(7, 3))
print(div(102, 3))
print(div(5, 35))
