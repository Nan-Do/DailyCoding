# How to solve it:
# Two part solution we will return the or of both.
# When b is 1 x must be x and 0 otherwise
# When b is 0 y must be y and 0 otherwise
# First part c = (b << x) - b
# This creates a mask of 0x111111 if b is 1 or 0 if b is 0
# (0 << x) - 0 or (1 << x) - 1
# The second part is easier
# y & 0 if b is 1
# y & -1 if b is 0 -1 is  e
def return_x_or_y(x, y, b):
    c = (b << x) - b
    return (x & c) | (y & (b - 1))

 s
print(return_x_or_y(31, 5, 1))
print(return_x_or_y(3, 8, 0))
